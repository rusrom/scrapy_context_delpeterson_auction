# Scrapy spider with using Item Loader Context<br/>Custom filenames for images<br/>Download images on AWS S3

Spider has 1 input argumet **auction ID** that can be founded in auction URL(red area)

![argument](https://i.imgur.com/kMp4Rl7.jpg)

**_All lots are scraping with ONLY 1 REQUEST_** with usings GET parameter perPage(blue area).

### Scrape such fields
1. Lot Number
2. Lot Description
3. City
4. State
5. ZIP
6. Seller Contact
7. Seller Phone
8. Category
9. Auction ClosesOn

![delpeterson](https://i.imgur.com/xvwiymn.png)

### Path for saving images
Each auction URL has **auctionId** GET parameter(red area)  
![argument](https://i.imgur.com/m0bvkQo.jpg)

For each auction on AWS S3 folder will be created with corresponding name

![aws](https://i.imgur.com/gHsGHVz.jpg)

### Rule for images names
* 1st digit - lot number
* 2nd digit - image index
* All images need download on Amazon S3

Filenames for 5 images of lot number 1:  
1_1.jpg, 1_2.jpg, 1_3.jpg, 1_4.jpg, 1_5.jpg

![lot_photos](https://i.imgur.com/pp6DLUb.jpg)
