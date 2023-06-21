import streamlit as st

st.title('Datasets')

import streamlit as st

dataset_dict = {
    "Fish Vision": "https://kaggle.com/datasets/f91244f2af70a56d09cfe2b93d5c2aed44072921cddfda7d5ad630805ff872e2",
    "Deep Fish": "https://www.kaggle.com/datasets/vencerlanz09/deep-fish-object-detection",
    "Marine Debris": "https://universe.roboflow.com/neural-ocean/neural_ocean",
    "Marine Garbage": "https://conservancy.umn.edu/handle/11299/214865",
    "Fishing Vessels": "https://huggingface.co/spaces/competitions/ship-detection",
    "Marine Animals": "https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste",
    "Coral reef": "https://www.kaggle.com/datasets/vencerlanz09/healthy-and-bleached-corals-image-classification",
    "TACO dataset": "https://www.kaggle.com/datasets/vencerlanz09/taco-dataset-yolo-format",
}

for dataset_name, dataset_link in dataset_dict.items():
    st.markdown(f"[{dataset_name}]({dataset_link})")


from font_utils.poppins import make_font_poppins
make_font_poppins()