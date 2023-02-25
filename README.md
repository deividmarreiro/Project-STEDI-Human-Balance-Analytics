# Project-STEDI-Human-Balance-Analytics 💻

Hello there! And welcome to my third project about data engineering. 

In this one, we'll use some things in AWS as S3, Athena and Glue.

For use this project, you need to follow the steps bellow.
<br><br>

## First of all 1️⃣

You need to open the `/data` folder, there contains the data to run in this project.

Although, the data provided in there is malformed, so follow the instructions of the folder.

## Second 2️⃣

Confiture a `.aws` folder or export the credentials to run the next steps.

## Third 3️⃣

Enter the `terraform` folder and follow the instructions to set the enviroment on AWS

## And finally 🔚

Run the command bellow 

```sh
# This will send to the data from the `/data/trusted` to the S3
make start
```

## How to use 🧑‍🏫

Well, this project was maded to run in the AWS Console, so get the code em the `sql` folder to create the landing tables.
And create Glue Jobs with the `.py` files in the folder `jobs`

That's all! 😊