import numpy as np
import pandas as pd
import random as r


def top_n_products(n, min_interaction=50):
    final_rating = pd.read_csv("final_rating1.csv")

    # Finding products with minimum number of interactions
    recommendations = final_rating[final_rating["rating_count"] > min_interaction]

    # Sorting values w.r.t average rating
    recommendations = recommendations.sort_values("avg_rating", ascending=False)

    # print(recommendations.head())
    return recommendations["prod_id"].head(n)


def update_rating(prod_asin="A2CX7LUOHB2NDG", users_id="0321732944"):

    # Create a new DataFrame to append
    new_data = pd.DataFrame(
        {
            "user_id": [users_id],
            "prod_id": [prod_asin],
            "rating": [float(r.randint(1, 5))],
        },
    )
    # Append the data to the CSV file
    new_data.to_csv("ratings_Electronics.csv", mode="a", header=False, index=False)
    print("Updated")


def refresh_the_ratings():

    df = pd.read_csv(
        "ratings_Electronics.csv", header=None
    )  # There are no headers in the data file

    df.columns = ["user_id", "prod_id", "rating", "timestamp"]  # Adding column names

    df = df.drop("timestamp", axis=1)  # Dropping timestamp

    df_copy = df.copy(deep=True)  # Copying the data to another dataframe

    counts = df["user_id"].value_counts()
    df_final = df[df["user_id"].isin(counts[counts >= 50].index)]

    # Creating the interaction matrix of products and users based on ratings and replacing NaN value with 0
    final_ratings_matrix = df_final.pivot(
        index="user_id", columns="prod_id", values="rating"
    ).fillna(0)

    # Calculate the average rating for each product
    average_rating = df_final.groupby("prod_id")["rating"].mean()

    # Calculate the count of ratings for each product
    count_rating = df_final.groupby("prod_id")["rating"].count()

    # Create a dataframe with calculated average and count of ratings
    final_rating = pd.DataFrame(
        {"avg_rating": average_rating, "rating_count": count_rating}
    )

    # Sort the dataframe by average of ratings
    final_rating = final_rating.sort_values(by="avg_rating", ascending=False)

    final_rating.head()
    final_rating.to_csv("final_rating1.csv")


if __name__ == "__main__":
    refresh_the_ratings()
