import streamlit as st
import requests


st.set_page_config(page_title="🍽️ Vaishali's Cooking App", layout="centered")
st.title("👩‍🍳 Vaishali's Cooking App")
st.markdown("Search for recipes using **any ingredient** via TheMealDB API.")


ingredient = st.text_input("Enter an ingredient:", placeholder="e.g. chicken, egg, rice")

def fetch_meals_by_ingredient(ingredient):
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(url)
    if response.ok:
        return response.json().get("meals")
    return None


def fetch_meal_details(meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(url)
    if response.ok:
        return response.json().get("meals")[0]
    return None

if ingredient:
    meals = fetch_meals_by_ingredient(ingredient)
    if meals:
        st.success(f"Found {len(meals)} meal(s) with '{ingredient}' 🍴")
        for meal in meals:
            with st.expander(meal["strMeal"]):
                st.image(meal["strMealThumb"], width=300)
                if st.button(f"Show Recipe for {meal['strMeal']}", key=meal['idMeal']):
                    meal_details = fetch_meal_details(meal["idMeal"])
                    if meal_details:
                        st.markdown(f"### {meal_details['strMeal']}")
                        st.markdown(f"**Category**: {meal_details['strCategory']} | **Area**: {meal_details['strArea']}")
                        st.image(meal_details["strMealThumb"], width=400)


                        # Ingredients
                        st.markdown("#### Ingredients")
                        ingredients = []
                        for i in range(1, 21):
                            ing = meal_details.get(f"strIngredient{i}")
                            measure = meal_details.get(f"strMeasure{i}")
                            if ing and ing.strip():
                                ingredients.append(f"- {ing} — {measure}")
                        st.markdown("\n".join(ingredients))


                        # Instructions
                        st.markdown("#### Instructions")
                        st.write(meal_details["strInstructions"])


                        # YouTube Video
                        if meal_details.get("strYoutube"):
                            st.video(meal_details["strYoutube"])

        else:
            st.warning("No meals found. Try a more common ingredient.")
