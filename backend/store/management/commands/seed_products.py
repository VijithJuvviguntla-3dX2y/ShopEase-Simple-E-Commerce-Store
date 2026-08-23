from django.core.management.base import BaseCommand  # type: ignore

from store.models import Product


class Command(BaseCommand):

    help = "Adds 30 sample products to the database"

    def handle(self, *args, **kwargs):

        products = [

            {
                "name": "Smart Watch Pro",
                "description": "Modern smartwatch with fitness tracking, notifications, activity monitoring and a stylish design for everyday use.",
                "price": 3999,
                "category": "Electronics",
                "stock": 30,
                "image": "https://www.sammobile.com/wp-content/uploads/2022/08/Galaxy-Watch-5-Pro-1-1.jpg",
            },

            {
                "name": "Bluetooth Speaker",
                "description": "Portable Bluetooth speaker delivering clear audio and strong bass. Ideal for home, travel and outdoor entertainment.",
                "price": 1799,
                "category": "Electronics",
                "stock": 40,
                "image": "https://i5.walmartimages.com/asr/a1f6e0c7-e42b-43ae-b3ce-980e16959109.90434e9998b717ab30fa4ac63173071a.jpeg",
            },

            {
                "name": "Gaming Mouse",
                "description": "Responsive gaming mouse with accurate tracking, comfortable grip and programmable buttons for gaming and everyday computer use.",
                "price": 1299,
                "category": "Electronics",
                "stock": 50,
                "image": "https://m.media-amazon.com/images/I/61qN9d08hgL._AC_.jpg",
            },

            {
                "name": "Mechanical Gaming Keyboard",
                "description": "Mechanical keyboard designed for gaming and productivity with responsive keys and a durable construction.",
                "price": 3499,
                "category": "Electronics",
                "stock": 20,
                "image": "https://www.gravastar.com/cdn/shop/files/75-mechanical-keyboard-gaming-wireless-RGB-gravastar-mercury-k1pro-cyberpunk-2.jpg?v=1735196173&width=1200",
            },

            {
                "name": "USB-C Fast Charger",
                "description": "Compact fast charger compatible with a wide range of USB-C devices. Designed for efficient everyday charging.",
                "price": 899,
                "category": "Electronics",
                "stock": 60,
                "image": "https://m.media-amazon.com/images/I/71O-F0u-5mL._AC_.jpg",
            },

            {
                "name": "Power Bank 20000mAh",
                "description": "High-capacity portable power bank suitable for charging smartphones, tablets and other compatible devices while traveling.",
                "price": 1599,
                "category": "Electronics",
                "stock": 35,
                "image": "https://m.media-amazon.com/images/I/61liDz9uZWL.jpg",
            },

            {
                "name": "Wireless Earbuds",
                "description": "Compact wireless earbuds offering convenient listening, clear audio and a comfortable fit for everyday use.",
                "price": 2199,
                "category": "Electronics",
                "stock": 45,
                "image": "https://images.priceoye.pk/m20-tws-wireless-bluetooth-earbuds-pakistan-priceoye-zniaz.jpg",
            },

            {
                "name": "Laptop Backpack",
                "description": "Durable laptop backpack with multiple compartments for laptops, books, accessories and everyday essentials.",
                "price": 1899,
                "category": "Accessories",
                "stock": 35,
                "image": "https://m.media-amazon.com/images/I/91YandYecdL.jpg",
            },

            {
                "name": "Men's Casual T-Shirt",
                "description": "Comfortable casual T-shirt made for everyday wear. Features a simple modern design suitable for multiple occasions.",
                "price": 799,
                "category": "Clothing",
                "stock": 80,
                "image": "https://i5.walmartimages.com/seo/Enridrech-Men-s-Casual-Tee-Shirts-Comfortable-Short-Sleeve-Tees-Tops-for-Men-Casual-Fashion-Color-Block-Striped-Shirt_903f5f54-2235-43f3-8e80-c502b7285d0b.22e16fc5836aa13d64cd66d6e746485d.jpeg?odnHeight=573&odnWidth=573&odnBg=FFFFFF",
            },

            {
                "name": "Men's Denim Jacket",
                "description": "Classic denim jacket with a versatile design that pairs well with casual outfits and everyday clothing.",
                "price": 2499,
                "category": "Clothing",
                "stock": 30,
                "image": "https://i5.walmartimages.com/seo/Levi-s-Men-s-Denim-Trucker-Jacket_e956615c-5f71-4f27-950f-3b3460ed05e3_1.822afa92300b8dea0395359b9404f2e6.jpeg",
            },

            {
                "name": "Men's Formal Shirt",
                "description": "Smart formal shirt suitable for office wear, meetings and professional occasions.",
                "price": 1299,
                "category": "Clothing",
                "stock": 50,
                "image": "https://i5.walmartimages.com/seo/Zylanna-Men-s-Formal-Dress-Shirts-Button-Long-Sleeve-Business-Solid-Turn-Down-Collar-Shirts-White-Size-L_d5951c3d-938b-4ebd-80b2-03cc7e33c0a1.5abd60d912a2adbcfb7ad04e1d6eb3f0.jpeg",
            },

            {
                "name": "Women's Casual T-Shirt",
                "description": "Comfortable women's casual T-shirt with a modern style suitable for everyday activities.",
                "price": 899,
                "category": "Clothing",
                "stock": 60,
                "image": "https://img.ltwebstatic.com/images3_pi/2024/02/22/8f/17086039009a323ff9f746314308a911d36282efaa_thumbnail_900x.webp",
            },

            {
                "name": "Women's Summer Dress",
                "description": "Lightweight summer dress with a stylish design suitable for casual outings, events and warm-weather occasions.",
                "price": 1799,
                "category": "Clothing",
                "stock": 40,
                "image": "https://img.ltwebstatic.com/images3_pi/2023/12/07/d2/170195141020b8f3f3cedf6fde53d5c36a691b893c_thumbnail_900x.webp",
            },

            {
                "name": "Women's Denim Jacket",
                "description": "Stylish denim jacket designed for casual outfits and comfortable everyday wear.",
                "price": 2299,
                "category": "Clothing",
                "stock": 25,
                "image": "https://i5.walmartimages.com/seo/Clearance-Women-s-Denim-Jackets-Women-s-Basic-Solid-Color-Button-Down-Denim-Cotton-Jacket-With-Pockets-Denim-Jacket-Coat_cd4f3cbf-52ae-4fd4-a370-7f55705c79d4.aa37619d0789801a312a8ed7178e8762.jpeg",
            },

            {
                "name": "Running Shoes",
                "description": "Lightweight running shoes designed for comfortable walking, jogging and everyday fitness activities.",
                "price": 2999,
                "category": "Footwear",
                "stock": 35,
                "image": "https://s3.amazonaws.com/www.irunfar.com/wp-content/uploads/2023/07/24133535/Best-Trail-Running-Shoes-Brooks-Cascadia-17.jpg",
            },

            {
                "name": "Casual Sneakers",
                "description": "Modern casual sneakers combining comfort and style for everyday wear, college and outings.",
                "price": 2499,
                "category": "Footwear",
                "stock": 45,
                "image": "https://5.imimg.com/data5/SELLER/Default/2022/11/KE/VX/MV/116453489/white-casual-shoes-for-men-1000x1000.jpg",
            },

            {
                "name": "Sports Shoes",
                "description": "Comfortable sports shoes designed for workouts, sports activities and active lifestyles.",
                "price": 3299,
                "category": "Footwear",
                "stock": 30,
                "image": "https://static.vecteezy.com/system/resources/previews/046/323/598/non_2x/pair-of-colorful-sports-shoes-for-active-lifestyle-png.png",
            },

            {
                "name": "Men's Formal Shoes",
                "description": "Elegant formal shoes designed for office wear, business meetings and special occasions.",
                "price": 2899,
                "category": "Footwear",
                "stock": 25,
                "image": "https://tse3.mm.bing.net/th/id/OIP.IzbLfSmAB6r4cEE37Oz6swHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
            },

            {
                "name": "Women's Running Shoes",
                "description": "Lightweight athletic shoes designed for running, walking and daily fitness activities.",
                "price": 2799,
                "category": "Footwear",
                "stock": 35,
                "image": "https://img.kwcdn.com/product/1dec4a1170/5162f26f-308e-4081-8604-e86edbc4ffe1_800x800.jpeg.a.jpg",
            },

            {
                "name": "Leather Wallet",
                "description": "Compact and stylish wallet designed to organize cards, cash and identification documents.",
                "price": 999,
                "category": "Accessories",
                "stock": 70,
                "image": "https://axwellwallet.com/cdn/shop/articles/1_6f546ab4-cf86-4948-92cc-a84e62177b80.png?v=1740524292&width=1800",
            },

            {
                "name": "Classic Sunglasses",
                "description": "Stylish sunglasses with a classic design suitable for casual outings, travel and everyday use.",
                "price": 1299,
                "category": "Accessories",
                "stock": 50,
                "image": "https://dtpmhvbsmffsz.cloudfront.net/posts/2015/03/10/54ffcd79fa2b286cfc072b1f/m_54ffcd79fa2b286cfc072b22.jpg",
            },

            {
                "name": "Leather Belt",
                "description": "Classic leather belt with a durable design suitable for formal and casual outfits.",
                "price": 899,
                "category": "Accessories",
                "stock": 60,
                "image": "https://tse1.explicit.bing.net/th/id/OIP.XiDBZDuH4cxhCriKSo6bWwHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
            },

            {
                "name": "Analog Wrist Watch",
                "description": "Classic analog wristwatch with a stylish appearance suitable for formal and casual occasions.",
                "price": 2499,
                "category": "Accessories",
                "stock": 25,
                "image": "https://img.drz.lazcdn.com/static/lk/p/2342acd0c61091f937fc3580db284c2b.jpg_720x720q80.jpg",
            },

            {
                "name": "Travel Duffel Bag",
                "description": "Spacious travel duffel bag designed to carry clothing, accessories and personal belongings during trips.",
                "price": 1999,
                "category": "Accessories",
                "stock": 40,
                "image": "https://m.media-amazon.com/images/I/71WT7KlABQL._AC_SL1500_.jpg",
            },

            {
                "name": "Table Lamp",
                "description": "Modern table lamp providing comfortable lighting for study areas, bedrooms, offices and workspaces.",
                "price": 1299,
                "category": "Home",
                "stock": 30,
                "image": "https://i5.walmartimages.com/seo/Cinkeda-Modern-Table-Lamp-Set-of-2-for-Bedroom-Living-Room-with-USB-A-C-Ports-AC-Outlet-Gradient-Grey-Glass-Nightlight-Nightstand-Bedside-Lamps_67db5344-6a74-4a5a-93db-3d90a6882c0c.d5c2021820f2529074f231880651de1f.jpeg",
            },

            {
                "name": "Modern Wall Clock",
                "description": "Modern wall clock designed to add a clean and stylish touch to homes, offices and study rooms.",
                "price": 999,
                "category": "Home",
                "stock": 45,
                "image": "https://imagecdn.99acres.com/microsite/wp-content/blogs.dir/6161/files/2023/07/Wooden-wall-clock-5-2.jpg",
            },

            {
                "name": "Ceramic Coffee Mug",
                "description": "Durable ceramic coffee mug suitable for tea, coffee, hot chocolate and everyday beverages.",
                "price": 499,
                "category": "Home",
                "stock": 100,
                "image": "https://m.media-amazon.com/images/I/81lfJTcw06L._AC_SL1500_.jpg",
            },

            {
                "name": "Stainless Steel Water Bottle",
                "description": "Reusable stainless steel water bottle designed to keep drinks convenient and portable throughout the day.",
                "price": 799,
                "category": "Home",
                "stock": 75,
                "image": "https://m.media-amazon.com/images/I/61r+sMUv1lL._AC_SL1500_.jpg",
            },

            {
                "name": "Office Desk Organizer",
                "description": "Practical desk organizer for keeping pens, stationery and small office accessories neat and accessible.",
                "price": 699,
                "category": "Home",
                "stock": 55,
                "image": "https://m.media-amazon.com/images/I/81opOsQb3JL.jpg",
            },
        ]

        created_count = 0
        updated_count = 0

        for product_data in products:

            _product, created = Product.objects.update_or_create(
                name=product_data["name"],
                defaults=product_data
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\nSuccessfully processed {len(products)} products."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Created: {created_count}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Updated: {updated_count}"
            )
        )