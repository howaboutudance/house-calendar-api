"""uuid notify trigger

Revision ID: 0ff88225f044
Revises: 3e93b8e5c168
Create Date: 2022-09-07 18:00:25.613223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0ff88225f044"
down_revision = "3e93b8e5c168"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
    CREATE OR REPLACE FUNCTION notify_new_event_id()
        RETURNS TRIGGER
        LANGUAGE plpgsql
        AS $body$
        BEGIN
            PERFORM pg_notify(
                'event_id_feed',
                json_build_object(
                    'id', NEW.id::text,
                    'name',NEW.name::text
                    )::text
            );
            RETURN NEW;
        END
        $body$;
    """
    )

    op.execute(
        """
    CREATE OR REPLACE TRIGGER new_event_push
    AFTER INSERT
    ON event
    FOR EACH ROW
    EXECUTE FUNCTION notify_new_event_id();
    """
    )


def downgrade():
    op.execute("DROP TRIGGER new_event_push ON event")
    op.execute("DROP FUNCTION notify_new_event_id()")
