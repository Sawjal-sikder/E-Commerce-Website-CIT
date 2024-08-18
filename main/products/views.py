from django.shortcuts import render
from .models import Product,SubCategory, Category
from django.core.paginator import Paginator
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from django.http import FileResponse
import io
import random

# Create your views here.
def products(requests):
    pass



def single_product(requests, slug):
    product_len = len(Product.objects.all())
    start = random.randint(0,product_len)
    end = start+5
    Products = Product.objects.all().order_by('-created')[start:end]
    one_product = Product.objects.get(slug=slug)
    dis_amount = one_product.old_price - one_product.new_price
    pers = dis_amount / one_product.new_price *100
    subcategories = Category.objects.all()
    all_products = Product.objects.filter(category=one_product.category)
    return render(requests, 'single_product.html',
                  {
                      'one_product':one_product,
                      'subcategories':subcategories,
                      'all_products':all_products,
                      'dis_amount':pers,
                      'Products':Products,
                  })

def shop_grid_right(request):
    Productsa = Product.objects.all().order_by('-created')[0:3]
    numbers_of = [5, 10, 15, 20]
    categories = Category.objects.all()
    shop_list = Product.objects.all()

    # Get sorting option from query parameter
    sort_by = request.GET.get('sort', 'default')

    # Apply sorting based on the selected option
    if sort_by == 'price_low_to_high':
        shop_list = shop_list.order_by('new_price')
    elif sort_by == 'price_high_to_low':
        shop_list = shop_list.order_by('-new_price')
    elif sort_by == 'release_date':
        shop_list = shop_list.order_by('-created')
    elif sort_by == 'avg_rating':
        shop_list = shop_list.order_by('-avg_rating')  # assuming avg_rating is a field in your model

    # Get the 'per_page' parameter
    per_page = request.GET.get('per_page', 5)
    if per_page == 'all':
        page_obj = shop_list
    else:
        paginator = Paginator(shop_list, per_page)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    return render(request, 'shop_grid_right.html', {
        'page_obj': page_obj,
        'shop_list': shop_list,
        'categories': categories,
        'per_page': per_page,
        'numbers_of': numbers_of,
        'sort_by': sort_by,
        'Productsa' : Productsa,
    })

def search_category(request, name):
    Categorie = Category.objects.get(name=name)
    Products = Product.objects.filter(category=Categorie)
    shop_list = Products
    paginators = Paginator(shop_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginators.get_page(page_number)
    return render(request, 'shop_grid_right.html', {
        'page_obj': page_obj, 'shop_list': shop_list,
    })


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)

    # Define the data for the table
    data = [["Name", "Category", "Price", "Stock"]]  # Table headers
    products = Product.objects.all()

    for product in products:
        data.append([
            product.name,
            product.category.name,
            f"${product.new_price:.2f}",
            str(product.stock)
        ])

    # Create the table object
    table = Table(data)

    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Draw the table on the PDF
    table.wrapOn(p, inch, inch)
    table.drawOn(p, inch, 9 * inch - len(data) * 0.25 * inch)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="products.pdf")
