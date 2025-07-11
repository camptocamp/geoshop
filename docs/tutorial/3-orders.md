# Part 2 - Order a product

At this point in the tutorial, you should have:
 * A validated client account
 * A product listed in the catalog

## Placing an Order

1. Navigate to the frontend at [https://localhost/en](https://localhost/en).
2. Add the product to your cart and draw a polygon on the map.
3. Click the cart icon in the top right corner and select ***Proceed to checkout...***.
4. If prompted, log in with your user account.
5. Fill out the required fields and select ***Public*** for ***Type of mandate***.

:::tip
The type of order you choose will affect how the price is calculated. For public mandates, all products are free. For private mandates, prices will be determined by the backend based on the selected products.
:::

6. Click the <Badge type="tip" text="Next" /> button.
7. Click the <Badge type="tip" text="Confirm order" /> button.

As a client, you will be redirected to the My Orders page, where the status of your order should display as "Extraction in progress."

The order will also be visible in the admin interface at https://localhost/api/admin. In a production environment, you do not need to take any action, as the Extract process will automatically check for products to be extracted. However, we have not configured Extract yet.
