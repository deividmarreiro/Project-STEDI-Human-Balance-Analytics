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

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-stedi-data-lakehouse/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="StepTrainerLanding_node1",
)

# Script generated for node Customer Curated
CustomerCurated_node1677326046166 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-stedi-data-lakehouse/customer/curated/"],
        "recurse": True,
    },
    transformation_ctx="CustomerCurated_node1677326046166",
)

# Script generated for node Renamed keys for ApplyMapping
RenamedkeysforApplyMapping_node1677326182050 = ApplyMapping.apply(
    frame=CustomerCurated_node1677326046166,
    mappings=[
        ("serialNumber", "string", "`(right) serialNumber`", "string"),
        (
            "shareWithPublicAsOfDate",
            "long",
            "`(right) shareWithPublicAsOfDate`",
            "long",
        ),
        ("birthDay", "string", "`(right) birthDay`", "string"),
        ("registrationDate", "long", "`(right) registrationDate`", "long"),
        (
            "shareWithResearchAsOfDate",
            "long",
            "`(right) shareWithResearchAsOfDate`",
            "long",
        ),
        ("customerName", "string", "`(right) customerName`", "string"),
        ("email", "string", "`(right) email`", "string"),
        ("lastUpdateDate", "long", "`(right) lastUpdateDate`", "long"),
        ("phone", "string", "`(right) phone`", "string"),
        (
            "shareWithFriendsAsOfDate",
            "long",
            "`(right) shareWithFriendsAsOfDate`",
            "long",
        ),
    ],
    transformation_ctx="RenamedkeysforApplyMapping_node1677326182050",
)

# Script generated for node Join Step Trainer Landing to Customer Curated
JoinStepTrainerLandingtoCustomerCurated_node2 = Join.apply(
    frame1=StepTrainerLanding_node1,
    frame2=RenamedkeysforApplyMapping_node1677326182050,
    keys1=["serialNumber"],
    keys2=["`(right) serialNumber`"],
    transformation_ctx="JoinStepTrainerLandingtoCustomerCurated_node2",
)

# Script generated for node Drop Fields
DropFields_node1677326205189 = DropFields.apply(
    frame=JoinStepTrainerLandingtoCustomerCurated_node2,
    paths=[
        "`(right) serialNumber`",
        "`(right) shareWithPublicAsOfDate`",
        "`(right) birthDay`",
        "`(right) registrationDate`",
        "`(right) shareWithResearchAsOfDate`",
        "`(right) customerName`",
        "`(right) email`",
        "`(right) lastUpdateDate`",
        "`(right) phone`",
        "`(right) shareWithFriendsAsOfDate`",
    ],
    transformation_ctx="DropFields_node1677326205189",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node3 = glueContext.getSink(
    path="s3://udacity-stedi-data-lakehouse/step_trainer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="StepTrainerTrusted_node3",
)
StepTrainerTrusted_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="step_trainer_trusted"
)
StepTrainerTrusted_node3.setFormat("json")
StepTrainerTrusted_node3.writeFrame(DropFields_node1677326205189)
job.commit()
