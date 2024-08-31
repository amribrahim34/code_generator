class RelationshipHelper:
    @staticmethod
    def get_relationship_method(relation_type, related_model):
        """
        Generate the relationship method based on the relation type and related model.
        """
        method_name = related_model.lower()
        if relation_type in ['hasMany', 'belongsToMany']:
            method_name = f"{method_name}s"
        
        return f"""
    public function {method_name}()
    {{
        return $this->{relation_type}({related_model}::class);
    }}
"""

    @staticmethod
    def get_foreign_key(model_name, relation_type):
        """
        Generate the foreign key name based on the model name and relation type.
        """
        if relation_type == 'belongsTo':
            return f"{model_name.lower()}_id"
        return 'id'

    @staticmethod
    def get_pivot_table_name(model1, model2):
        """
        Generate the pivot table name for many-to-many relationships.
        """
        models = sorted([model1.lower(), model2.lower()])
        return f"{models[0]}_{models[1]}"

    @staticmethod
    def get_inverse_relation(relation_type):
        """
        Get the inverse relation type.
        """
        inverse_relations = {
            'hasOne': 'belongsTo',
            'hasMany': 'belongsTo',
            'belongsTo': 'hasOne',
            'belongsToMany': 'belongsToMany'
        }
        return inverse_relations.get(relation_type, 'belongsTo')

    @staticmethod
    def should_add_foreign_key(relation_type):
        """
        Determine if a foreign key should be added for this relation type.
        """
        return relation_type in ['belongsTo', 'hasOne', 'hasMany']

