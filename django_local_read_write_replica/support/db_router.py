class DatabaseRouter:
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Always read from REPLICA database
        """
        return "replica"

    def db_for_write(self, model, **hints):
        """
        Always write to DEFAULT database
        """
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Objects from REPLICA and DEFAULT are de same, then True always
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Only DEFAULT database
        """
        return db == "default"
