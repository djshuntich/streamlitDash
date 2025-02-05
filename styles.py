def apply_custom_styles():
    return """
        <style>
        /* Set background image */
        .stApp {
            background-image: url('attached_assets/background5.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .stButton>button {
            background-color: #FEE960;
            color: #032844;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            font-weight: bold;
        }

        .stTextInput>div>div>input {
            background-color: #012239;
            color: #FEFEFB;
            border: 1px solid #FEE960;
            border-radius: 4px;
        }

        .stDataFrame {
            background-color: #012239;
        }

        .css-1d391kg {
            background-color: #011B2D;
        }

        /* Style sidebar */
        .css-1m3wtmm {
            background-color: rgba(1, 27, 45, 0.9);
            padding: 2rem 1rem;
        }

        /* Style metrics */
        .css-1xarl3l {
            background-color: rgba(1, 34, 57, 0.9);
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #FEE960;
        }

        /* Style main container */
        .main .block-container {
            background-color: rgba(1, 27, 45, 0.9);
            padding: 2rem;
            border-radius: 10px;
        }

        .stProgress .st-bo {
            background-color: #FEE960;
        }

        /* Center logo in login page */
        .element-container img {
            margin: 0 auto;
            display: block;
        }
        </style>
    """