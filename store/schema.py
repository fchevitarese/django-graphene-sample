import graphene

from .models import Category


class ProductType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    picture = graphene.String()
    category = graphene.String()


class CategoryType(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    description = graphene.String()
    products = graphene.List(ProductType)
    product_count = graphene.String()

    @graphene.resolve_only_args
    def resolve_products(self):
        return self.product_category.all()

    @graphene.resolve_only_args
    def resolve_product_count(self):
        return self.product_category.all().count()


class QueryType(graphene.ObjectType):
    all_categories = graphene.List(
        CategoryType,
        description='Return all categories'
    )

    category = graphene.Field(CategoryType, id=graphene.String())

    @graphene.resolve_only_args
    def resolve_all_categories(self):
        return Category.objects.all()

    @graphene.resolve_only_args
    def resolve_category(self, id):
        return Category.objects.get(pk=id)


schema = graphene.Schema(query=QueryType)

# query {
#   allCategories{
#     id
#     name
#     description
#     products{
#       id
#       name
#       description
#       picture
#       category
#     }
#   }
# }

# query {
#   category(id: "1"){
#     name
#     description
#     products{
#       name
#       picture
#       description
#     }
#   }

# }
