
import joblib
import pandas as pd


def test_saved_model():

    package = joblib.load("wine_classifier.joblib")

    required_keys = {
        "model",
        "feature_names",
        "target_names",
        "feature_defaults",
        "feature_minimums",
        "feature_maximums",
        "sklearn_version"
    }

    assert required_keys.issubset(package.keys())

    model = package["model"]
    feature_names = package["feature_names"]
    target_names = package["target_names"]
    defaults = package["feature_defaults"]

    sample = pd.DataFrame(
        [[defaults[feature] for feature in feature_names]],
        columns=feature_names
    )

    prediction = model.predict(sample)[0]
    probabilities = model.predict_proba(sample)[0]

    assert len(feature_names) == 13
    assert prediction in range(len(target_names))
    assert len(probabilities) == len(target_names)
    assert abs(probabilities.sum() - 1.0) < 1e-6

    print("All model tests passed successfully.")


if __name__ == "__main__":
    test_saved_model()
