"""post complete

Revision ID: d9d3b63cb30f
Revises: 97e434534f20
Create Date: 2023-02-27 04:14:31.405554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9d3b63cb30f'
down_revision = '97e434534f20'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(),server_default= "True", nullable= False))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default= sa.text("now()"), nullable= False))
    
    pass


def downgrade() -> None:
    op.drop_column("post", "published")
    op.drop_column("post", "created_at")
    pass
