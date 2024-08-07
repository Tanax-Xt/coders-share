"""many to many

Revision ID: 65dfeb98301b
Revises: fb48042b62f4
Create Date: 2024-04-19 20:28:01.634851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "65dfeb98301b"
down_revision: Union[str, None] = "fb48042b62f4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "basket",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "basket_to_projects",
        sa.Column("basket", sa.Integer(), nullable=True),
        sa.Column("projects", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["basket"],
            ["basket.id"],
        ),
        sa.ForeignKeyConstraint(
            ["projects"],
            ["projects.id"],
        ),
    )
    op.create_table(
        "bought_projects_to_user",
        sa.Column("projects", sa.Integer(), nullable=True),
        sa.Column("users", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["projects"],
            ["projects.id"],
        ),
        sa.ForeignKeyConstraint(
            ["users"],
            ["users.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("bought_projects_to_user")
    op.drop_table("basket_to_projects")
    op.drop_table("basket")
    # ### end Alembic commands ###
