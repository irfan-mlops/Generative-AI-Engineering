import streamlit as st


EXERCISES = [
    ("Barbell Squat", "Legs", "Intermediate", "🏋️", "4 sets × 8–10 reps"),
    ("Push-ups", "Chest", "Beginner", "💪", "3 sets × 12–15 reps"),
    ("Lat Pulldown", "Back", "Beginner", "🔥", "3 sets × 10–12 reps"),
    ("Shoulder Press", "Shoulders", "Intermediate", "⚡", "3 sets × 8–12 reps"),
    ("Walking Lunges", "Legs", "Beginner", "🚶", "3 sets × 12 reps"),
    ("Plank", "Core", "Beginner", "🎯", "3 sets × 30–45 seconds"),
]


def setup_page():
    st.set_page_config(
        page_title="FitZone Gym",
        page_icon="🏋️",
        layout="wide"
    )


def add_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0c111b;
            color: #f4f7fb;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
        }

        [data-testid="stSidebar"] {
            background-color: #111927;
        }

        h1, h2, h3 {
            color: #f4f7fb !important;
        }

        .hero {
            background: linear-gradient(120deg, #1d342a, #17243a);
            border: 1px solid #345444;
            border-radius: 22px;
            padding: 40px;
            margin-bottom: 30px;
        }

        .hero h1 {
            font-size: 3rem;
            line-height: 1.15;
        }

        .accent {
            color: #a9f266;
        }

        .muted {
            color: #abb7c9;
        }

        .card {
            background-color: #151f2e;
            border: 1px solid #2a3648;
            border-radius: 16px;
            padding: 22px;
            min-height: 170px;
            margin-bottom: 16px;
        }

        .card h3 {
            margin: 10px 0 5px;
        }

        .tag {
            color: #a9f266;
            font-weight: bold;
            font-size: 0.85rem;
            margin-top: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def show_card(title, description, icon, detail=""):
    st.markdown(
        f"""
        <div class="card">
            <div style="font-size: 2rem;">{icon}</div>
            <h3>{title}</h3>
            <div class="muted">{description}</div>
            <div class="tag">{detail}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def sidebar_menu():
    with st.sidebar:
        st.markdown("## ⚡ FITZONE")
        st.divider()

        page = st.radio(
            "Navigation",
            ["Home", "Exercises", "Workout Plan", "About"]
        )

        st.divider()
        st.caption("TRAIN STRONG • FEEL BETTER")

    return page


def home_page():
    st.markdown(
        """
        <div class="hero">
            <p class="accent"><b>YOUR FITNESS STARTS HERE</b></p>
            <h1>Build strength.<br>
            <span class="accent">Become your best.</span></h1>
            <p class="muted">
                Explore exercises and follow a simple weekly workout plan.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Explore Your Training")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_card(
            "Exercise Library",
            "Browse exercises by muscle group",
            "🏋️",
            "6 EXERCISES"
        )

    with col2:
        show_card(
            "Weekly Plan",
            "Follow a simple training schedule",
            "📅",
            "3 WORKOUT DAYS"
        )

    with col3:
        show_card(
            "Stay Motivated",
            "Improve one workout at a time",
            "🎯",
            "KEEP GOING"
        )

    st.subheader("Today's Motivation")
    st.info("Progress starts with showing up. Move at your own pace.")


def exercises_page():
    st.title("Exercise Library")
    st.write("Explore exercises for different muscle groups.")

    col1, col2 = st.columns([1, 2])

    with col1:
        selected_group = st.selectbox(
            "Muscle group",
            ["All", "Legs", "Chest", "Back", "Shoulders", "Core"]
        )

    with col2:
        search = st.text_input(
            "Search exercise",
            placeholder="Type an exercise name..."
        )

    filtered_exercises = [
        exercise for exercise in EXERCISES
        if (selected_group == "All" or exercise[1] == selected_group)
        and search.lower() in exercise[0].lower()
    ]

    if not filtered_exercises:
        st.warning("No exercises found.")
        return

    for start in range(0, len(filtered_exercises), 3):
        columns = st.columns(3)

        for column, exercise in zip(
            columns,
            filtered_exercises[start:start + 3]
        ):
            name, group, level, icon, sets = exercise

            with column:
                show_card(
                    name,
                    f"{group} • {level}",
                    icon,
                    sets
                )


def workout_plan_page():
    st.title("Weekly Workout Plan")
    st.write("A simple three-day gym routine.")

    plan = [
        (
            "Monday — Upper Body",
            "Push-ups • Lat Pulldown • Shoulder Press",
            "💪"
        ),
        (
            "Wednesday — Lower Body",
            "Barbell Squat • Walking Lunges • Plank",
            "🦵"
        ),
        (
            "Friday — Full Body",
            "Squat • Push-ups • Plank",
            "🔥"
        ),
    ]

    for title, exercises, icon in plan:
        show_card(title, exercises, icon, "45–60 MINUTES")

    st.info("Use the other days for rest or light activity.")


def about_page():
    st.title("About FitZone")

    st.markdown(
        """
        <div class="hero">
            <p class="accent"><b>TRAIN WITH PURPOSE</b></p>
            <h1>Simple fitness.<br>
            <span class="accent">Clear direction.</span></h1>
            <p class="muted">
                FitZone is a gym website design created with Streamlit.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "This design includes a home page, exercise library, "
        "search and filters, and a weekly workout plan."
    )


def main():
    setup_page()
    add_styles()

    page = sidebar_menu()

    if page == "Home":
        home_page()
    elif page == "Exercises":
        exercises_page()
    elif page == "Workout Plan":
        workout_plan_page()
    else:
        about_page()


if __name__ == "__main__":
    main()