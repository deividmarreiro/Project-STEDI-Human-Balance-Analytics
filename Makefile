start:
	aws s3 sync ./data/trusted/customers/ s3://udacity-stedi-data-lakehouse/customers/landing && \
	aws s3 sync ./data/trusted/accelerometer/ s3://udacity-stedi-data-lakehouse/accelerometer/landing && \
	aws s3 sync ./data/trusted/step_trainer/ s3://udacity-stedi-data-lakehouse/step_trainer/landing