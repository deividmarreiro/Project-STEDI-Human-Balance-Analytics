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

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-stedi-data-lakehouse/step_trainer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="StepTrainerTrusted_node1",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1677327832713 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://udacity-stedi-data-lakehouse/accelerometer/trusted/"],
        "recurse": True,
    },
    transformation_ctx="AccelerometerTrusted_node1677327832713",
)

# Script generated for node Join Step Trainer Trusted to Accelerometer Trusted
JoinStepTrainerTrustedtoAccelerometerTrusted_node2 = Join.apply(
    frame1=StepTrainerTrusted_node1,
    frame2=AccelerometerTrusted_node1677327832713,
    keys1=["sensorReadingTime"],
    keys2=["timeStamp"],
    transformation_ctx="JoinStepTrainerTrustedtoAccelerometerTrusted_node2",
)

# Script generated for node Drop Fields
DropFields_node1677327881482 = DropFields.apply(
    frame=JoinStepTrainerTrustedtoAccelerometerTrusted_node2,
    paths=["user", "timeStamp", "x", "y", "z"],
    transformation_ctx="DropFields_node1677327881482",
)

# Script generated for node Step Trainer Curated
StepTrainerCurated_node3 = glueContext.getSink(
    path="s3://udacity-stedi-data-lakehouse/step_trainer/curated/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="StepTrainerCurated_node3",
)
StepTrainerCurated_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="step_trainer_curated"
)
StepTrainerCurated_node3.setFormat("json")
StepTrainerCurated_node3.writeFrame(DropFields_node1677327881482)
job.commit()
