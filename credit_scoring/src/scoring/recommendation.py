import pandas as pd


def generate_recommendations(detailed_breakdown):
    """
    Generate improvement recommendations based on low-scoring features.

    Parameters
    ----------
    detailed_breakdown : dict
        Output from calculate_score_breakdown().

    Returns
    -------
    pd.DataFrame
        Recommendations table.
    """

    recommendation_data = []

    for component, features in detailed_breakdown.items():

        for feature_name, feature_info in features.items():

            score = feature_info.get("score", 0)
            value = feature_info.get("value", "N/A")

            # Only focus on weaker areas
            if score <= 2:

                recommendation = ""

                if "Debt" in feature_name or "DTI" in feature_name:
                    recommendation = (
                        "Reduce debt obligations to improve repayment capacity."
                    )

                elif "Payment" in feature_name:
                    recommendation = (
                        "Improve repayment discipline by making payments on time."
                    )

                elif "Savings" in feature_name:
                    recommendation = "Increase savings consistently to strengthen financial resilience."

                elif "Employment" in feature_name:
                    recommendation = "Maintain stable employment for a longer period."

                elif "Income" in feature_name:
                    recommendation = (
                        "Improve income stability or diversify income sources."
                    )

                elif "Expense" in feature_name:
                    recommendation = "Reduce monthly expenses to improve affordability."

                elif "Application" in feature_name:
                    recommendation = "Avoid frequent credit applications."

                elif "Living" in feature_name:
                    recommendation = "Maintain residential stability."

                else:
                    recommendation = (
                        "Improve this area to strengthen the overall credit profile."
                    )

                recommendation_data.append(
                    {
                        "Component": component,
                        "Feature": feature_name,
                        "Current Value": value,
                        "Rating": feature_info.get("reason", ""),
                        "Recommendation": recommendation,
                    }
                )

    return pd.DataFrame(recommendation_data)
