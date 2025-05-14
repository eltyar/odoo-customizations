{
    'name': 'تكلفة المنتج وهامش الربح في أمر البيع',
    'version': '1.0',
    'summary': 'إضافة تكلفة المنتج وهامش الربح في سطور أوامر البيع',
    'description': """
        هذه الوحدة تضيف حقول تكلفة المنتج وهامش الربح في سطور أوامر البيع.
        تعتمد هذه الوحدة على وحدة sale_margin الموجودة في أودو.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Sales',
    'depends': [
        'sale',
        'sale_margin',
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
