import graphene

from .models import Category, Product


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

    all_products = graphene.List(
        ProductType,
        description='Return all products'
    )

    product = graphene.Field(ProductType, id=graphene.Int())
    product_by_name = graphene.Field(ProductType, name=graphene.String())

    @graphene.resolve_only_args
    def resolve_all_categories(self):
        return Category.objects.all()

    @graphene.resolve_only_args
    def resolve_category(self, id):
        return Category.objects.get(pk=id)

    @graphene.resolve_only_args
    def resolve_all_products(self):
        return Product.objects.all()

    @graphene.resolve_only_args
    def resolve_product(self, id):
        return Product.objects.get(pk=id)

    @graphene.resolve_only_args
    def resolve_product_by_name(self, name):
        return Product.objects.get(name=name)


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
