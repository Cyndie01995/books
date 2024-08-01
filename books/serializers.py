from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    intro = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ( 'name', 'author', 'date_published')
        
    def get_intro(self, obj):
        name = obj.name
        author = obj.author
        
        intro = f'This book {name} was written by {author}'
        return intro 
    # or write return f'name {obj.name} written by {obj.author}
       
        
    def get_price(self, obj):
        # return 0
        # if there is a default value that will be returned as zero
        # number_pages = getattr(obj, 'number_pages',0)
        number_of_pages = obj.number_of_pages
        number_of_chapters = obj.number_of_chapters
        
        price = int(number_of_pages) * int(number_of_chapters)
        return price  # 10% discount for purchases of more than 1000 pages
       