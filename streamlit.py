
# import re
# import requests
# import streamlit as st


# # ---------- Page configuration ----------

# st.set_page_config(
#     page_title="AI Investment Advisor",
#     page_icon="📈",
#     layout="wide"
# )

# st.title("📈 AI Investment Advisor")
# st.caption("Personalized asset allocation and ETF recommendations")


# # ---------- Sidebar: API settings ----------

# with st.sidebar:
#     st.header("Settings")

#     api_url = st.text_input(
#         "API base URL",
#         value="http://127.0.0.1:8000"
#     )

#     timeout = st.slider(
#         "Request timeout (seconds)",
#         min_value=10,
#         max_value=180,
#         value=90
#     )

#     st.info(
#         "Start your FastAPI backend first:\n\n"
#         "`uvicorn app:app --reload`"
#     )


# # ---------- Input form ----------

# with st.form("invest_form"):

#     col1, col2 = st.columns(2)

#     with col1:

#         age = st.number_input(
#             "Age",
#             min_value=18,
#             max_value=100,
#             value=30,
#             step=1
#         )

#         goal = st.selectbox(
#             "Goal",
#             [
#                 "Wealth growth",
#                 "Retirement",
#                 "Buy a house",
#                 "Child's education",
#                 "Regular income",
#                 "Capital preservation"
#             ]
#         )

#     with col2:

#         horizon = st.number_input(
#             "Investment horizon (years)",
#             min_value=1,
#             max_value=60,
#             value=10,
#             step=1
#         )

#         risk = st.selectbox(
#             "Risk tolerance",
#             ["low", "medium", "high"],
#             index=1
#         )

#     submitted = st.form_submit_button(
#         "Get my plan",
#         type="primary",
#         use_container_width=True
#     )


# # ---------- Extract allocation percentages ----------

# def extract_allocation(text):
#     """
#     Extract asset allocation percentages from the LLM response.

#     Example:
#     | Stocks | 70% |
#     | Bonds | 25% |
#     | Cash | 5% |
#     """

#     rows = []

#     pattern = re.compile(
#         r"\|\s*\**([^|]+?)\**\s*\|\s*\**(\d+(?:\.\d+)?)%\**\s*\|"
#     )

#     for line in str(text).splitlines():

#         match = pattern.search(line)

#         if match:

#             asset = match.group(1).strip()
#             percentage = float(match.group(2))

#             if percentage <= 100:
#                 rows.append((asset, percentage))

#     return rows


# # ---------- Call FastAPI ----------

# if submitted:

#     payload = {
#         "age": int(age),
#         "goal": goal,
#         "horizon": int(horizon),
#         "risk": risk
#     }

#     try:

#         with st.spinner("Analyzing your profile..."):

#             response = requests.post(
#                 f"{api_url.rstrip('/')}/invest",
#                 json=payload,
#                 timeout=timeout
#             )

#             response.raise_for_status()

#             data = response.json()

#         st.session_state["result"] = data

#     except requests.exceptions.ConnectionError:

#         st.error(
#             "Could not connect to the FastAPI backend. "
#             "Make sure the backend server is running."
#         )

#     except requests.exceptions.Timeout:

#         st.error(
#             "The request timed out. "
#             "Try increasing the timeout in the sidebar."
#         )

#     except requests.exceptions.HTTPError:

#         st.error(
#             f"FastAPI returned an error: {response.status_code}"
#         )

#         st.code(response.text)

#     except Exception as e:

#         st.error(f"Something went wrong: {e}")


# # ---------- Show results ----------

# data = st.session_state.get("result")


# if data:

#     st.divider()

#     # ---------- Profile ----------

#     st.subheader("👤 Your Profile")

#     profile = data.get("profile")

#     if isinstance(profile, dict):

#         cols = st.columns(len(profile))

#         for col, (key, value) in zip(cols, profile.items()):

#             col.metric(
#                 key.replace("_", " ").title(),
#                 str(value)
#             )

#     else:

#         st.write(profile)


#     # ---------- Results ----------

#     tab1, tab2 = st.tabs(
#         ["📊 Allocation", "💰 ETF Recommendations"]
#     )


#     # ---------- Allocation tab ----------

#     with tab1:

#         allocation_text = data.get("allocation", "")

#         rows = extract_allocation(allocation_text)

#         if rows:

#             left, right = st.columns(2)

#             with left:

#                 st.subheader("Asset Allocation")

#                 chart_data = {
#                     name: percentage
#                     for name, percentage in rows
#                 }

#                 st.bar_chart(
#                     chart_data,
#                     horizontal=True
#                 )

#             with right:

#                 st.subheader("Allocation Details")

#                 st.dataframe(
#                     [
#                         {
#                             "Asset Class": name,
#                             "Allocation (%)": percentage
#                         }
#                         for name, percentage in rows
#                     ],
#                     hide_index=True,
#                     use_container_width=True
#                 )

#         st.markdown(allocation_text)


#     # ---------- ETF recommendations tab ----------

#     with tab2:

#         recommendations = data.get(
#             "recommendations",
#             ""
#         )

#         st.markdown(recommendations)


#     # ---------- Disclaimer ----------

#     st.caption(
#         "For educational purposes only. "
#         "This is not financial advice."
#     )


import re
import requests
import streamlit as st


st.set_page_config(
    page_title="AI Investment Advisor",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Investment Advisor")
st.caption("Personalized asset allocation and ETF recommendations")


with st.sidebar:
    st.header("Settings")

    api_url = st.text_input(
        "API base URL",
        value="http://127.0.0.1:8000"
    )

    timeout = st.slider(
        "Request timeout (seconds)",
        min_value=10,
        max_value=180,
        value=90
    )

    st.info(
        "Start your FastAPI backend first:\n\n"
        "`uvicorn app:app --reload`"
    )


with st.form("invest_form"):

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30,
            step=1
        )

        goal = st.selectbox(
            "Goal",
            [
                "Wealth growth",
                "Retirement",
                "Buy a house",
                "Child's education",
                "Regular income",
                "Capital preservation"
            ]
        )

    with col2:

        horizon = st.number_input(
            "Investment horizon (years)",
            min_value=1,
            max_value=60,
            value=10,
            step=1
        )

        risk = st.selectbox(
            "Risk tolerance",
            ["low", "medium", "high"],
            index=1
        )

    submitted = st.form_submit_button(
        "Get my plan",
        type="primary",
        use_container_width=True
    )


def extract_allocation(text):

    rows = []

    pattern = re.compile(
        r"\|\s*\**([^|]+?)\**\s*\|\s*\**(\d+(?:\.\d+)?)%\**\s*\|"
    )

    for line in str(text).splitlines():

        match = pattern.search(line)

        if match:

            asset = match.group(1).strip()
            percentage = float(match.group(2))

            if percentage <= 100:
                rows.append((asset, percentage))

    return rows


if submitted:

    payload = {
        "age": int(age),
        "goal": goal,
        "horizon": int(horizon),
        "risk": risk
    }

    try:

        with st.spinner("Analyzing your profile..."):

            response = requests.post(
                f"{api_url.rstrip('/')}/invest",
                json=payload,
                timeout=timeout
            )

            response.raise_for_status()

            data = response.json()

        st.session_state["result"] = data

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to the FastAPI backend. "
            "Make sure the backend server is running."
        )

    except requests.exceptions.Timeout:

        st.error(
            "The request timed out. "
            "Try increasing the timeout in the sidebar."
        )

    except requests.exceptions.HTTPError:

        st.error(
            f"FastAPI returned an error: {response.status_code}"
        )

        st.code(response.text)

    except Exception as e:

        st.error(f"Something went wrong: {e}")


data = st.session_state.get("result")


if data:

    st.divider()

    st.subheader("👤 Your Profile")

    profile = data.get("profile")

    if isinstance(profile, dict):

        cols = st.columns(len(profile))

        for col, (key, value) in zip(cols, profile.items()):

            col.metric(
                key.replace("_", " ").title(),
                str(value)
            )

    else:

        st.write(profile)


    tab1, tab2 = st.tabs(
        ["📊 Allocation", "💰 ETF Recommendations"]
    )


    with tab1:

        allocation_text = data.get("allocation", "")

        rows = extract_allocation(allocation_text)

        if rows:

            left, right = st.columns(2)

            with left:

                st.subheader("Asset Allocation")

                chart_data = {
                    name: percentage
                    for name, percentage in rows
                }

                st.bar_chart(
                    chart_data,
                    horizontal=True
                )

            with right:

                st.subheader("Allocation Details")

                st.dataframe(
                    [
                        {
                            "Asset Class": name,
                            "Allocation (%)": percentage
                        }
                        for name, percentage in rows
                    ],
                    hide_index=True,
                    use_container_width=True
                )

        st.markdown(allocation_text)


    with tab2:

        recommendations = data.get(
            "recommendations",
            ""
        )

        st.markdown(recommendations)


    st.caption(
        "For educational purposes only. "
        "This is not financial advice."
    )
