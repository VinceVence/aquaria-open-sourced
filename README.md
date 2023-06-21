# Aquaria: A Web-Based AI Platform 🐟

Aquaria is a web-based AI platform that leverages Convolutional Neural Networks (CNNs) and the YOLOv8 algorithm to enable precision fishing, aquaculture, and marine sustainability practices in the Philippines. This platform provides a comprehensive set of computer vision services, including object detection, image classification, and synthetic image generation, to assist users in optimizing fishing practices and promoting marine conservation.
## 🚀Key Features 

- Object detection: Utilize state-of-the-art computer vision algorithms to detect and localize objects of interest in images or video streams. :mag_right:
- Image classification: Classify images into predefined categories to identify marine species, fishing vessels, or other relevant objects. :fish:
- Synthetic image generation: Generate synthetic images by combining foreground and background images, enabling various simulations and training scenarios. :paintbrush:
- User-friendly interface: Access Aquaria through mobile phones or web browsers, making it accessible and convenient for users. :iphone: :computer:
- Streamlit deployment: The Aquaria platform is deployed on Streamlit, providing a seamless and interactive web-based experience. :globe_with_meridians:
- Data management: Split datasets into training, validation, and testing sets, and apply data augmentation techniques to enhance model performance. :file_folder:
- Transfer learning: Fine-tune pre-trained models to adapt to specific marine animals and marine debris classification tasks. :brain:
- Documentation: Comprehensive documentation, including guidelines for data preparation, model training, and usage of the Aquaria platform. :book:

## 📂Datasets

Aquaria leverages several publicly available datasets to train and evaluate its computer vision models. The following datasets have been used in the development of Aquaria:

- [Fish Vision Dataset](https://kaggle.com/datasets/f91244f2af70a56d09cfe2b93d5c2aed44072921cddfda7d5ad630805ff872e2)
- [Deep Fish Dataset](https://www.kaggle.com/datasets/vencerlanz09/deep-fish-object-detection)
- [Marine Debris Dataset](https://universe.roboflow.com/neural-ocean/neural_ocean)
- [Marine Garbage Dataset](https://conservancy.umn.edu/handle/11299/214865)
- [Fishing Vessels Dataset](https://huggingface.co/spaces/competitions/ship-detection)
- [Marine Animals Dataset](https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste) 
- [TACO Dataset](https://www.kaggle.com/datasets/vencerlanz09/taco-dataset-yolo-format)

Please refer to the respective dataset links for more information on their content and licensing terms.

## ⚙️Installation 

To install and run Aquaria locally, please follow these steps:

1. Clone the Aquaria repository: `git clone https://github.com/VinceVence/aquaria.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Aquaria application: `streamlit run app.py`

Ensure that you have Python 3.7 or later installed on your system.


## 🖥️Usage

1. Accessing Aquaria:
   - Upon opening the Aquaria link, you will be prompted to enter a password.
   - For this guide, the password is 'admin'. Enter the password and proceed to the Aquaria homepage.

2. The Homepage:
   - The Aquaria homepage serves as an overview page providing an outline of the state of fisheries, AI, and technology in the Philippines.

3. Navigation:
   - On the left of the homepage, you will find a sidebar containing various tabs that lead to the different services provided by Aquaria.

4. Accessing Services:
   - To access the computer vision services, click on the 'Service' tab. If the model weights for the chosen service are not yet downloaded, Aquaria will automatically download them.

5. Model Download:
   - If the weights are already downloaded, you will see the message: '🚀Models Successfully Loaded'.

6. Using a Service:
   - After the model weights have been downloaded, you can now access and use the services. Select the desired service.
   - For instance, if you select the 'Fish Vision Service', you will be directed to the Fish Vision Service page.

7. Uploading an Image:
   - On the Fish Vision Service page, you will be prompted to upload a photo. Click on the 'Browse Files' button, select your photo, and confirm your selection to upload the image. You may also choose to drag-and-drop your photo.

8. Model Processing and Results Display:
   - Once the image is successfully uploaded, the computer vision model processes the image in the background and subsequently displays the predicted output to the user.

You can now use Aquaria to analyze your marine images using our AI-powered computer vision models.


## 🤝Contributing 

We welcome contributions to Aquaria! To contribute, please follow these steps:

1. Fork the Aquaria repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`
3. Make your modifications and commit your changes: `git commit -m "Description of changes"`
4. Push your branch to your forked repository: `git push origin feature-name`
5. Submit a pull request to the main Aquaria repository.

## 📝License

Aquaria is released under the [MIT License](https://opensource.org/licenses/MIT).

## 📧Contact

For any inquiries or support, please contact the Aquaria author at the following email: **lanz.vencer@lpunetwork.edu.ph**
