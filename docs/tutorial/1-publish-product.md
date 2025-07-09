# GeoShop Tutorial

In this tutorial, we will publish a product, place an order as a client, and configure Extract to manage data extraction.

If you have followed the [getting started](./getting-started) guide, you should be able to access your API at:

https://localhost/api

Click on the Admin button and log in using the default credentials:

* user: admin
* password: Test1234

## Part 1 - Publish your first product

### Create a Metadata

You cannot create a product without *Metadata*. *Metadata* contains all the information about the geodata, such as its description, category, and contacts, while the *Product* includes technical attributes that make the product orderable, like pricing and data formats.

*Metadata* is stored in a separate table, and you can import metadata from an existing catalog; however, this feature is not part of GeoShop.

1. Under ***API*** section, click on the <Badge type="info" text="+Add" /> link for ***Metadatas***
2. Fill in the some fields:
   * Set ***Id_name*** to `swiss_municipalities`.  It's a textual unique identifier, compare this to a collection identifier as specified in OGC API Features
   * Set ***Name*** to `Swiss municipalities` A user-friendly name
   * ***Description_long***: Basic HTML is supported here, copy paste this:
   ```html
   A sample dataset which goal is:<br>
   • Demonstrate the capabilities of the GeoShop<br>
   • Example of data extraction from Extract<br>
   <span style="color: red;">⚠ THIS DATASET IS ONLY FOR TESTING PURPOSES</span>
   ```

Click on the <Badge type="tip" text="SAVE" /> button, the metadata is created. [Read more on metadatas](../documentation/metadata)

### Create a Product

1. In the left navigation bar, click on the <Badge type="info" text="+ Add" />  link of ***Products***
2. Clic on the 🔍 next to ***Metadata*** field and select the metadata we just add
3. ***Label*** it to `Swiss Municipalities`. This will be the visible name on the catalog
4. Set the ***Product_statu**s* to `Published`
5. Select the existing ***Provider*** `external_provider`
6. Add a new pricing by clicking on the <Badge type="info" text="➕" /> icon:
   1. Let's name it `Free`
   2. Set ***Princing_type*** as `Free`
   3. Set all prices to `0`
   4. Click <Badge type="tip" text="SAVE" /> button
7. Scroll down to ***PRODUCT_FORMATS*** section and click on the <Badge type="info" text="➕" /> to add a new one:
   1. Name it `Geopackage`
   2. Click <Badge type="tip" text="SAVE" /> button
8. In the ***PRODUCT OWNERSHIPS*** section, set ***USER_GROUP*** to `extract`
9. Click on the <Badge type="tip" text="SAVE" /> button to create your product.

Now, if you navigate to the home page of your project at https://localhost/en, the product should be visible in the catalog.
