from components.quiz_ui import render_question_block, show_feedback
from components.quiz_component import get_score, reset_quiz_state # noqa
import streamlit as st

def render_quiz(quiz_data, key_prefix="quiz"):
    """
    Renders a quiz block with questions, options, and feedback.

    Parameters:
    - quiz_data: List of dicts with 'question', 'options', 'answer'
    - key_prefix: Unique prefix for Streamlit widget keys
    """

    st.markdown("### 🧠 Quiz Time")

    score = 0
    for i, q in enumerate(quiz_data):
        question_key = f"{key_prefix}_{i}"
        selected = render_question_block(q["question"], q["options"], key=question_key)

        if selected:
            is_correct = selected == q["answer"]
            show_feedback(is_correct)
            score += int(is_correct)

    st.divider()
    st.success(f"🏆 Your Score: {score} / {len(quiz_data)}")

    if st.button("🔄 Reset Quiz"):
        reset_quiz_state(len(quiz_data), key_prefix)
        st.experimental_rerun()

# from components.quiz_ui import render_question_block, show_feedback
# from components.quiz_component import get_score, reset_quiz_state
# import streamlit as st

# def render_quiz(quiz_data, key_prefix="quiz"):
#     """
#     Renders a quiz block with questions, options, and feedback.

#     Parameters:
#     - quiz_data: List of dicts with 'question', 'options', 'answer'
#     - key_prefix: Unique prefix for Streamlit widget keys
#     """

#     st.markdown("### 🧠 Quiz Time")

#     score = 0
#     for i, q in enumerate(quiz_data):
#         question_key = f"{key_prefix}_{i}"
#         selected = render_question_block(q["question"], q["options"], key=question_key)

#         if selected:
#             is_correct = selected == q["answer"]
#             show_feedback(is_correct)
#             score += int(is_correct)

#     st.divider()
#     st.success(f"🏆 Your Score: {score} / {len(quiz_data)}")

#     if st.button("🔄 Reset Quiz"):
#         reset_quiz_state(len(quiz_data), key_prefix)
#         st.experimental_rerun()

# # from quiz_ui import render_question_block, show_feedback
# # from quiz_component import get_score, reset_quiz_state
# # import streamlit as st

# # def render_quiz(quiz_data, key_prefix="quiz"):
# #     """
# #     Renders a quiz block with questions, options, and feedback.

# #     Parameters:
# #     - quiz_data: List of dicts with 'question', 'options', 'answer'
# #     - key_prefix: Unique prefix for Streamlit widget keys
# #     """

# #     st.markdown("### 🧠 Quiz Time")

# #     score = 0
# #     for i, q in enumerate(quiz_data):
# #         question_key = f"{key_prefix}_{i}"
# #         selected = render_question_block(q["question"], q["options"], key=question_key)

# #         if selected:
# #             is_correct = selected == q["answer"]
# #             show_feedback(is_correct)
# #             score += int(is_correct)

# #     st.divider()
# #     st.success(f"🏆 Your Score: {score} / {len(quiz_data)}")

# #     if st.button("🔄 Reset Quiz"):
# #         reset_quiz_state(len(quiz_data), key_prefix)
# #         st.experimental_rerun()
