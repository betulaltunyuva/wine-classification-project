
import joblib
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Wine Classifier",
    page_icon="🍷",
    layout="wide"
)


@st.cache_resource
def load_model_package():
    return joblib.load("wine_classifier.joblib")


package = load_model_package()

model = package["model"]
feature_names = package["feature_names"]
target_names = package["target_names"]
feature_defaults = package["feature_defaults"]
feature_minimums = package["feature_minimums"]
feature_maximums = package["feature_maximums"]


st.title("🍷 Wine Classification Application")

st.write(
    """
    This application predicts the class of a wine sample according to
    its chemical properties. The prediction is produced using an
    optimized Logistic Regression model.
    """
)

st.info(
    "Enter the chemical measurements and press the prediction button."
)

input_values = {}

with st.form("wine_prediction_form"):

    left_column, right_column = st.columns(2)

    for index, feature in enumerate(feature_names):

        selected_column = (
            left_column if index % 2 == 0 else right_column
        )

        with selected_column:
            input_values[feature] = st.number_input(
                label=feature.replace("_", " ").title(),
                min_value=float(feature_minimums[feature]),
                max_value=float(feature_maximums[feature]),
                value=float(feature_defaults[feature]),
                format="%.4f"
            )

    predict_button = st.form_submit_button(
        "Predict Wine Class",
        use_container_width=True
    )


if predict_button:

    input_dataframe = pd.DataFrame(
        [input_values],
        columns=feature_names
    )

    prediction = model.predict(input_dataframe)[0]
    probabilities = model.predict_proba(input_dataframe)[0]

    predicted_class = target_names[prediction]

    st.success(
        f"Predicted wine class: **{predicted_class}**"
    )

    probability_dataframe = pd.DataFrame({
        "Class": target_names,
        "Probability": probabilities
    })

    st.subheader("Prediction Probabilities")
    st.dataframe(
        probability_dataframe.style.format({
            "Probability": "{:.2%}"
        }),
        use_container_width=True
    )

    st.bar_chart(
        probability_dataframe.set_index("Class")
    )


st.divider()

st.caption(
    "Developed for educational and machine-learning portfolio purposes."
)
