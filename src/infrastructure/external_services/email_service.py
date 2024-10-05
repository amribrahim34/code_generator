import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Any
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str, template_dir: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.jinja_env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

    async def send_email(self, to_email: str, subject: str, template_name: str, context: Dict[str, Any]) -> bool:
        try:
            template = self.jinja_env.get_template(template_name)
            html_content = template.render(context)

            message = MIMEMultipart()
            message["From"] = self.username
            message["To"] = to_email
            message["Subject"] = subject

            message.attach(MIMEText(html_content, "html"))

            async with aiosmtplib.SMTP(hostname=self.smtp_server, port=self.smtp_port, use_tls=True) as smtp:
                await smtp.login(self.username, self.password)
                await smtp.send_message(message)
            return True
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            return False

    async def send_welcome_email(self, to_email: str, username: str) -> bool:
        subject = "Welcome to Our Platform!"
        context = {
            "username": username,
            "login_url": "https://yourapp.com/login"
        }
        return await self.send_email(to_email, subject, "welcome.html", context)

    async def send_password_reset_email(self, to_email: str, reset_token: str) -> bool:
        subject = "Password Reset Request"
        context = {
            "reset_url": f"https://yourapp.com/reset-password?token={reset_token}",
            "expiry_time": "1 hour"
        }
        return await self.send_email(to_email, subject, "password_reset.html", context)

    async def send_subscription_confirmation_email(self, to_email: str, plan_name: str, features: List[str]) -> bool:
        subject = "Subscription Confirmation"
        context = {
            "plan_name": plan_name,
            "features": features
        }
        return await self.send_email(to_email, subject, "subscription_confirmation.html", context)

    async def send_project_generation_complete_email(self, to_email: str, project_name: str, download_url: str) -> bool:
        subject = "Project Generation Complete"
        context = {
            "project_name": project_name,
            "download_url": download_url
        }
        return await self.send_email(to_email, subject, "project_generated.html", context)

    async def send_bulk_email(self, to_emails: List[str], subject: str, template_name: str, context: Dict[str, Any]) -> Dict[str, bool]:
        results = {}
        for email in to_emails:
            success = await self.send_email(email, subject, template_name, context)
            results[email] = success
        return results