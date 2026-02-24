# Simple Text Extractor - English Version 1.1
**Available on Microsoft Store (Windows) • Available on Snap Store (Linux)**

# Copyright © Gaëtan Sencie 2025
# All rights reserved.

## Description

**Simple Text Extractor** is a fast, high-performance, and **100% offline** desktop OCR application. Securely extract text from your **PDF, PNG, JPG, JPEG, TIFF, or BMP** files while ensuring total privacy, as the application runs exclusively locally on your computer.

This **version 1.1** marks a major milestone with the introduction of **Linux (Ubuntu) support** via the **Snap Store** and a **"stateless" architecture**, guaranteeing maximum stability even during heavy processing tasks.

Validated and published on the **Microsoft Store and the Snap Store**, it offers a robust solution, a simple interface, and useful features such as **batch processing**. By leveraging the power of **Tesseract OCR**, **Simple Text Extractor** combines agility and data security for reliable and validated distribution.

## Preview

![Screenshot of the Simple-Text-Extractor app](https://github.com/STENS66/Simple-Text-Extractor/blob/main/images/image_app.png?raw=true)

### Compatibility

Desktop application designed for:

* **Windows**: 10 and 11 (64-bit).
* **Linux**: Available via Snap package on **Ubuntu** and compatible distributions.

### Features

- **Total Privacy:** All operations are performed locally without an internet connection.

- **Modern Interface:** New fluid and ergonomic graphical interface (based on CustomTkinter) with high-resolution screen support.

- **Batch Processing:** Add as many files as you wish to the queue and process them all automatically in sequence.

- **Drag & Drop:** Simply drag your files directly into the window to add them instantly.

- **Metadata Analysis:** Immediate visualization of technical details (Size, Page count, DPI Resolution, PDF/A Format) before processing.

- **Archiving Format (PDF/A):** Option to generate files compliant with the long-term archiving standard (PDF/A-1b).

- **Flexible Management:** Ability to remove files from the list one by one or clear everything in a single click.

- **Compatible:** Supports PDF, PNG, JPG, JPEG, TIFF, and BMP files.

- **Zero Configuration:** No administrator rights required, portable, and secure.

### Usage

To extract text with **"Simple Text Extractor"**:

**1. Add files:**

- Click the "Choose Input PDF or Image" button or simply drag your files (PDF or Images) into the application window.

**2. Configure output (Optional):**

- By default, files are saved in the same folder as the source.

- You can define a specific folder via the "Choose..." button in the Destination section.

- Check the "Archiving Format (PDF/A)" box if you want a document optimized for long-term preservation.

**3. Start processing:**

- Check the list of pending files.

- Click "Start OCR".

**4. Results:**

- Follow the global and detailed progress via the loading bar.

- Once finished, click the displayed links to directly open the folder containing your new files (automatically named with the _ocr suffix).

### Advantages

- **Enhanced Security:** Integrates protections against malicious files (Decompression Bombs) and secures internal process execution.

- **Industrial Stability:** Thanks to a new architecture (Multiprocessing), the application never freezes, even when processing heavy documents.

- **Simplicity:** Tooltips guide the user on every option.

- **Speed:** Optimized RAM processing for maximum execution speed.

- **Total Control:** The user retains absolute control over their files and information with no risk of leakage.

### Snap Store & Linux Specifics (Strict Confinement)

**Turnkey Experience**: The Linux (Snap) version is an **"all-in-one"** package under strict confinement. It comes pre-packaged with the **Tesseract OCR** engine and language dictionaries (**English, French, German, Dutch, Italian, Spanish, Portuguese, Chinese, Arabic, and Japanese**). No complex installation is required.

💡 **Tip:** Using Wayland? If Drag & Drop doesn't work, please use the "Add Files" button or switch to an X11 session.

⚠️ **Note regarding external drives (USB/SD)**: Since the application runs in a secured environment, it cannot access your external drives by default. If your files are stored on a USB flash drive or a second hard drive, you must grant access by running this command once in your terminal:


```
sudo snap connect simple-text-extractor:removable-media
```


## Download

- [Download from Microsoft Store](https://apps.microsoft.com/detail/9NVRKF4X80JZ?hl=en-us&gl=US)
- [![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/simple-text-extractor)
- Or via the terminal:

  ```
  sudo snap install simple-text-extractor

- [GitHub Releases](https://github.com/STENS66/Simple-Text-Extractor/releases)

## Contact

- Email: app.sencie@gmail.com
- LinkedIn: [Gaëtan Sencie](https://www.linkedin.com/in/ga%C3%ABtan-sencie-applications-python)
- GitHub: [STENS66](https://github.com/STENS66)

Thank you for using **"Simple Text Extractor"**!

---

## References & Keywords

Developed by **Gaëtan Sencie**, Python developer.

**Simple Text Extractor** is officially available on the **Microsoft Store**, **GitHub**, and the **Snap Store**, ensuring reliable and validated distribution.

**Keywords**: OCR, privacy, offline application, data security, PDF conversion, Tesseract, Tcl/Tk, Linux, Ubuntu, Snap Store, Python.

---

# Simple Text Extractor - Version française 1.1
**Disponible sur le Microsoft Store (Windows) • Disponible sur le Snap Store (Linux)**

# Copyright © Gaëtan Sencie 2025
# Tous droits réservés.


## Description

**Simple Text Extractor** est une application OCR de bureau rapide, performante et 100% hors ligne. Extrayez en toute sécurité le texte de vos fichiers **PDF, PNG, JPG, JPEG, TIFF ou BMP** tout en garantissant une confidentialité totale, puisque l'application fonctionne exclusivement en local sur votre ordinateur.

Cette **version 1.1** marque une étape majeure avec l'arrivée du **support Linux (Ubuntu)** via le Snap Store et une **architecture "stateless" (sans état)** garantissant une stabilité maximale, même lors de traitements lourds.

Validée et publiée sur le **Microsoft Store et le Snap Store**, elle offre une solution robuste, une interface simple et des fonctionnalités utiles comme le **traitement par lots**. En utilisant la puissance de **Tesseract OCR**, Simple Text Extractor combine agilité et sécurité des données pour une diffusion fiable et validée.

## Prévisualisation

![Capture d'écran de l'application Simple-Text-Extractor](https://github.com/STENS66/Simple-Text-Extractor/blob/main/images/image_app.png?raw=true)

### Compatibilité

Application de bureau conçue pour :

* **Windows** : 10 et 11 (64 bits).
* **Linux** : Disponible via paquet Snap sur **Ubuntu** et distributions compatibles.

### Fonctionnalités

- **Confidentialité Totale :** Toutes les opérations sont effectuées localement sans connexion internet.

- **Interface Moderne :** Nouvelle interface graphique fluide et ergonomique (basée sur CustomTkinter) avec support des écrans haute résolution.

- **Traitement par Lots (Batch Processing) :** Ajoutez autant de fichiers que vous le souhaitez dans la file d'attente et traitez-les tous automatiquement à la suite.

- **Glisser-Déposer (Drag & Drop) :** Glissez simplement vos fichiers directement dans la fenêtre pour les ajouter instantanément.

- **Analyse des Métadonnées :** Visualisation immédiate des détails techniques (Taille, Nombre de pages, Résolution DPI, Format PDF/A) avant le traitement.

- **Format Archivage (PDF/A) :** Option pour générer des fichiers conformes à la norme d'archivage long terme (PDF/A-1b).

- **Gestion Flexible :** Possibilité de supprimer des fichiers de la liste un par un ou de tout vider en un clic.

- **Compatible :** Prend en charge les fichiers PDF, PNG, JPG, JPEG, TIFF et BMP.

- **Zéro Configuration :** Aucun droit administrateur requis, portable et sécurisé.


### Utilisation

Pour extraire du texte avec **"Simple Text Extractor"** :

**1. Ajouter des fichiers :**

- Cliquez sur le bouton "Choisir PDF ou Image d'entrée" ou faites simplement glisser vos fichiers (PDF ou Images) dans la fenêtre de l'application.

**2. Configurer la sortie (Optionnel) :**

- Par défaut, les fichiers sont sauvegardés dans le même dossier que la source.

- Vous pouvez définir un dossier spécifique via le bouton "Choisir..." dans la section Destination.

- Cochez la case "Format Archivage (PDF/A)" si vous souhaitez un document optimisé pour la conservation longue durée.

**3. Lancer le traitement :**

- Vérifiez la liste des fichiers en attente.

- Cliquez sur "Lancer l'OCR".

**4. Résultats :**

- Suivez la progression globale et détaillée via la barre de chargement.

- Une fois terminé, cliquez sur les liens affichés pour ouvrir directement le dossier contenant vos nouveaux fichiers (nommés automatiquement avec le suffixe _ocr).


### Avantages

- **Sécurité Renforcée :** Intègre des protections contre les fichiers malveillants (Decompression Bombs) et sécurise l'exécution des processus internes.

- **Stabilité Industrielle :** Grâce à une nouvelle architecture (Multiprocessing), l'application ne gèle jamais, même lors du traitement de documents lourds.

- **Simplicité :** Des infobulles (tooltips) guident l'utilisateur sur chaque option.

- **Rapidité :** Traitement optimisé en mémoire vive (RAM) pour une vitesse d'exécution maximale.

- **Contrôle total :** L'utilisateur garde un contrôle absolu sur ses fichiers et informations sans risque de fuite.

### Spécificités Snap Store & Linux (Confinement Strict)

**Expérience Clé en Main** : La version Linux (Snap) est un paquet **"tout-en-un"** en confinement strict. Elle est livrée avec le moteur **Tesseract OCR** et les dictionnaires de langues (**Français,Anglais,Allemand,Néerlandais,Italien,Espagnol,Portugais,Chinois,Arabe et Japonais**). Aucune installation complexe n'est requise.

💡 **Astuce :** Vous utilisez Wayland ? Si le « Glisser-Déposer » ne fonctionne pas, veuillez utiliser le bouton « Ajouter des fichiers » ou passer à une session X11.

⚠️ **Note concernant les disques externes (USB/SD)** : L'application s'exécutant dans un environnement sécurisé, elle ne peut pas accéder à vos disques externes par défaut. Si vos fichiers sont stockés sur une clé USB ou un second disque dur, vous devez autoriser l'accès en exécutant cette commande une seule fois dans votre terminal :

```
sudo snap connect simple-text-extractor:removable-media
```

## Téléchargement

- [Télécharger depuis le Microsoft Store](https://apps.microsoft.com/detail/9NVRKF4X80JZ?hl=fr-be&gl=BE&ocid=pdpshare)
- [![Get it from the Snap Store](https://snapcraft.io/static/images/badges/fr/snap-store-black.svg)](https://snapcraft.io/simple-text-extractor)
  
- Ou via le terminal :


```
sudo snap install simple-text-extractor
```

## Contact

- Email : app.sencie@gmail.com
- LinkedIn : [Gaëtan Sencie](https://www.linkedin.com/in/ga%C3%ABtan-sencie-applications-python)
- GitHub : [STENS66](https://github.com/STENS66)

Merci d'utiliser **"Simple Text Extractor"** !

---

## Références & Mots-clés

Développé par **Gaëtan Sencie**, développeur Python.

**Simple Text Extractor** est officiellement disponible sur le **Microsoft Store**, **GitHub** et le **Snap Store**, garantissant une diffusion fiable et validée.

**Mots-clés** : Mots-clés : OCR, confidentialité, application hors ligne, sécurité des données, conversion PDF, Tesseract, Tcl/Tk, Linux, Ubuntu, Snap Store, Python.
