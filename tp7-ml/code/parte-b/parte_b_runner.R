library(randomForest)
library(dplyr)
library(ROSE)

base_filename <- "data/submissions/submission_"
index_filename <- 64

for (i in 1:10) {
    train_data <- read.csv("data/data-parte-b/train-data-FE.csv")
    test_data <- read.csv("data/data-parte-b/test-data-FE.csv")

    # balanceo de clases ---------------------------------------------------------------------------------------------------
    train_data <- ovun.sample(inclinacion_peligrosa ~ ., data = train_data, method = "under")$data  # default p = 0.5

    # class_distribution <- table(train_data$inclinacion_peligrosa)
    # class_probability <- class_distribution / sum(class_distribution)
    # class_weights <- class_distribution[2] / class_distribution

    # random forest --------------------------------------------------------------------------------------------------------

    # pasar a factor para hacerlo de clasificación
    # train_data$inclinacion_peligrosa <- factor(train_data$inclinacion_peligrosa)

    formula <- inclinacion_peligrosa ~ circ_tronco_cm + lat + long + peligrosidad_especie + peligrosidad_diametro + peligrosidad_altura
    rf_model <- randomForest(formula,
                             data = train_data,
                             do.trace = TRUE,
                             mtry = 3,  # Number of variables randomly sampled at each split. Default values: for classification sqrt(p) and regression p/3
                             # classwt = class_probability,
                             importance = TRUE,
                             proximity = TRUE,
                             ntree = 600
    )

    predictions <- predict(rf_model, test_data)
    predictions_numeric <- as.numeric(as.character(predictions)) # predictions es un factor, hay que pasarlo a numeric

    result_dataset <- data.frame(id = test_data$id, inclinacion_peligrosa = predictions_numeric)
    full_filename <- paste0(base_filename, index_filename, ".csv")
    write.csv(result_dataset, full_filename, row.names = FALSE)
    index_filename <- index_filename + 1
}