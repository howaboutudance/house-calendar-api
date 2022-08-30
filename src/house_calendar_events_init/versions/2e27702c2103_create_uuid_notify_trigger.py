"""create uuid notify trigger

Revision ID: 2e27702c2103
Revises: 3e93b8e5c168
Create Date: 2021-11-01 20:27:01.212315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2e27702c2103"
down_revision = "3e93b8e5c168"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
    CREATE OR REPLACE FUNCTION push_event_function()
    RETURNS trigger
    LANGUAGE plpgsql AS
    $body$
        BEGIN
            SELECT pg_notify(
                CAST('event_id_feed' AS text),
                NEW.id
                ) from NEW;
            RETURN NEW;
        END;
    $body$;
    """
    )
    op.execute(
        """
    CREATE TRIGGER push_event_id
        AFTER INSERT
        ON event
        FOR EACH ROW
        EXECUTE FUNCTION push_event_function();
    """
    )


def downgrade():
    op.execute("DROP TRIGGER push_event_id")
    op.execute("DROP FUNCTION push_event_function")
