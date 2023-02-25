import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1677281443755 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_landing",
    transformation_ctx="AccelerometerLanding_node1677281443755",
)

# Script generated for node Customer Trusted
CustomerTrusted_node1677281499138 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": True},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-stedi-data-lakehouse/customer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="CustomerTrusted_node1677281499138",
)

# Script generated for node Join Accelerometer Landing to Customer Trusted
JoinAccelerometerLandingtoCustomerTrusted_node2 = Join.apply(
    frame1=AccelerometerLanding_node1677281443755,
    frame2=CustomerTrusted_node1677281499138,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="JoinAccelerometerLandingtoCustomerTrusted_node2",
)

# Script generated for node Drop Customer Trusted Fields
DropCustomerTrustedFields_node1677281553573 = DropFields.apply(
    frame=JoinAccelerometerLandingtoCustomerTrusted_node2,
    paths=[
        "email",
        "phone",
        "shareWithFriendsAsOfDate",
        "lastUpdateDate",
        "customerName",
        "shareWithResearchAsOfDate",
        "registrationDate",
        "birthDay",
        "shareWithPublicAsOfDate",
        "serialNumber",
    ],
    transformation_ctx="DropCustomerTrustedFields_node1677281553573",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node3 = glueContext.getSink(
    path="s3://udacity-stedi-data-lakehouse/accelerometer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AccelerometerTrusted_node3",
)
AccelerometerTrusted_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="accelerometer_trusted"
)
AccelerometerTrusted_node3.setFormat("json")
AccelerometerTrusted_node3.writeFrame(DropCustomerTrustedFields_node1677281553573)
job.commit()
