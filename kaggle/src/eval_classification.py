def eval_classification(model, X_train, y_train, X_test, y_test, model_name="model", results_frame=None,
                        pos_label=1, average="binary", roc_auc_average="macro"):
    
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, ConfusionMatrixDisplay, roc_auc_score
    import pandas as pd

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    print("Train Evaluation")
    print(classification_report(y_train, train_pred))
    ConfusionMatrixDisplay.from_predictions(y_train, train_pred, normalize="true", cmap="Blues")
    plt.show()

    print("Test Evaluation")
    print(classification_report(y_test, test_pred))
    ConfusionMatrixDisplay.from_predictions(y_test, test_pred, normalize="true", cmap="Greens")
    plt.show()

    results = pd.DataFrame(index=[model_name])
  
    results["train_acc"] = accuracy_score(y_train, train_pred)
    results["test_acc"] = accuracy_score(y_test, test_pred)
    results["train_prec"] = precision_score(y_train, train_pred, pos_label=pos_label, average=average)
    results["test_prec"] = precision_score(y_test, test_pred, pos_label=pos_label, average=average)
    results["train_recall"] = recall_score(y_train, train_pred, pos_label=pos_label, average=average)
    results["test_recall"] = recall_score(y_test, test_pred, pos_label=pos_label, average=average)
    results["train_f1"] = f1_score(y_train, train_pred, pos_label=pos_label, average=average)
    results["test_f1"] = f1_score(y_test, test_pred, pos_label=pos_label, average=average)
    results["train_auc"] = roc_auc_score(y_train, model.predict_proba(X_train)[:, 1], multi_class="ovr", average=roc_auc_average)
    results["test_auc"] = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1], multi_class="ovr", average=roc_auc_average)  


    if results_frame is not None:
        results = pd.concat([results_frame, results])

    return results