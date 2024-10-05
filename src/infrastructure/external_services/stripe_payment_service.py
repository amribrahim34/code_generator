import stripe
from typing import Dict, List
from asyncio import to_thread
from src.core.entities.user import User
from src.core.entities.plan import Plan

class StripePaymentService:
    def __init__(self, api_key: str):
        stripe.api_key = api_key

    async def create_customer(self, user: User) -> str:
        """Create a Stripe customer for a user."""
        return await to_thread(stripe.Customer.create,
            email=user.email,
            metadata={"user_id": user.id}
        )

    async def create_subscription(self, user: User, plan: Plan) -> Dict:
        """Create a subscription for a user."""
        customer = await self.get_or_create_customer(user)
        return await to_thread(stripe.Subscription.create,
            customer=customer.id,
            items=[{"price": plan.stripe_price_id}]
        )

    async def cancel_subscription(self, subscription_id: str) -> Dict:
        """Cancel a subscription."""
        return await to_thread(stripe.Subscription.delete, subscription_id)

    async def update_subscription(self, subscription_id: str, new_plan: Plan) -> Dict:
        """Update a subscription to a new plan."""
        return await to_thread(stripe.Subscription.modify,
            subscription_id,
            items=[{"price": new_plan.stripe_price_id}]
        )

    async def get_subscription(self, subscription_id: str) -> Dict:
        """Get details of a subscription."""
        return await to_thread(stripe.Subscription.retrieve, subscription_id)

    async def list_invoices(self, customer_id: str) -> List[Dict]:
        """List invoices for a customer."""
        invoices = await to_thread(stripe.Invoice.list, customer=customer_id)
        return invoices.data

    async def get_or_create_customer(self, user: User) -> stripe.Customer:
        """Get existing Stripe customer or create a new one."""
        customers = await to_thread(stripe.Customer.list, email=user.email)
        if customers.data:
            return customers.data[0]
        return await self.create_customer(user)

    async def create_checkout_session(self, user: User, plan: Plan) -> str:
        """Create a Stripe Checkout session for a plan."""
        customer = await self.get_or_create_customer(user)
        session = await to_thread(stripe.checkout.Session.create,
            customer=customer.id,
            payment_method_types=['card'],
            line_items=[{
                'price': plan.stripe_price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='https://example.com/cancel',
        )
        return session.id

    async def handle_webhook(self, payload: Dict, sig_header: str, webhook_secret: str) -> Dict:
        """Handle Stripe webhooks."""
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        except ValueError as e:
            raise ValueError('Invalid payload')
        except stripe.error.SignatureVerificationError as e:
            raise ValueError('Invalid signature')

        if event['type'] == 'customer.subscription.updated':
            subscription = event['data']['object']
            # Handle subscription update
            pass
        elif event['type'] == 'customer.subscription.deleted':
            subscription = event['data']['object']
            # Handle subscription cancellation
            pass
        elif event['type'] == 'invoice.payment_succeeded':
            invoice = event['data']['object']
            # Handle successful payment
            pass
        elif event['type'] == 'invoice.payment_failed':
            invoice = event['data']['object']
            # Handle failed payment
            pass

        return {'status': 'success'}

    async def create_usage_record(self, subscription_item_id: str, quantity: int) -> Dict:
        """Create a usage record for metered billing."""
        return await to_thread(stripe.SubscriptionItem.create_usage_record,
            subscription_item_id,
            quantity=quantity,
            timestamp=int(time.time())
        )