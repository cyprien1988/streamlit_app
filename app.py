# Titre de l'application Streamlit
st.title('Gestion des Notes des Etudiants par Ecole')
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Jeux de données pour 12 écoles différentes
data_schools = {
    "Ecole A": pd.DataFrame({
        "Nom": ["Alice", "Bob", "Charlie"],
        "Note": [15, 18, 14]
    }),
    "Ecole B": pd.DataFrame({
        "Nom": ["David", "Eva", "Fay"],
        "Note": [12, 16, 10]
    }),
    "Ecole C": pd.DataFrame({
        "Nom": ["George", "Hannah", "Igor"],
        "Note": [13, 17, 19]
    }),
    "Ecole D": pd.DataFrame({
        "Nom": ["Jack", "Karen", "Liam"],
        "Note": [11, 16, 15]
    }),
    "Ecole E": pd.DataFrame({
        "Nom": ["Mona", "Nina", "Oscar"],
        "Note": [20, 13, 14]
    }),
    "Ecole F": pd.DataFrame({
        "Nom": ["Paul", "Quinn", "Rita"],
        "Note": [12, 17, 18]
    }),
    "Ecole G": pd.DataFrame({
        "Nom": ["Sam", "Tina", "Ugo"],
        "Note": [14, 15, 13]
    }),
    "Ecole H": pd.DataFrame({
        "Nom": ["Victor", "Wendy", "Xander"],
        "Note": [19, 16, 17]
    }),
    "Ecole I": pd.DataFrame({
        "Nom": ["Yasmine", "Zoe", "Amir"],
        "Note": [10, 15, 13]
    }),
    "Ecole J": pd.DataFrame({
        "Nom": ["Boris", "Clara", "Dina"],
        "Note": [14, 16, 12]
    }),
    "Ecole K": pd.DataFrame({
        "Nom": ["Elena", "Fiona", "Gustav"],
        "Note": [18, 14, 15]
    }),
    "Ecole L": pd.DataFrame({
        "Nom": ["Hugo", "Isabelle", "Jackie"],
        "Note": [19, 17, 16]
    })
}

# Titre de l'application
st.title('Gestion des Notes des Etudiants')

# Sélectionner l'école à afficher
ecole_choisie = st.selectbox("Choisissez une école", list(data_schools.keys()))

# Afficher les données de l'école choisie
st.write(f"Notes des étudiants de {ecole_choisie} :")
st.dataframe(data_schools[ecole_choisie])

# Récupérer les données de l'école choisie
df = data_schools[ecole_choisie]

# Choix de la couleur du graphique
color_palette = st.selectbox("Choisissez une palette de couleurs", 
                             ["Blues_d", "Blues", "Set1", "Pastel", "Dark", "viridis", "coolwarm", 
                              "magma", "cubehelix", "Spectral", "inferno", "plasma", "YlGnBu", "twilight",
                              "coolwarm_r", "YlOrRd", "GnBu", "cividis", "RdBu"])

# Choix du type de graphique
chart_type = st.selectbox("Choisissez le type de graphique", 
                          ["Barres 2D", "Barres 3D", "Points", "Histogramme", "Boxplot", 
                           "Violin", "Area", "Heatmap", "Pairplot", "Courbe avec cercles", "Zigzag", "Diagramme Circulaire"])

# Filtrer les étudiants avec une note minimale (optionnel)
note_min = st.slider("Sélectionnez la note minimale", min_value=0, max_value=20, value=0, step=1)
df_filtered = df[df["Note"] >= note_min]

# Tracer le graphique en fonction du type choisi
plt.figure(figsize=(8, 5))

# Créer une palette de couleurs basée sur le nombre d'étudiants
colors = sns.color_palette(color_palette, len(df_filtered))

# Tracer le graphique selon le type choisi
if chart_type == "Barres 2D":
    sns.barplot(x=df_filtered["Nom"], y=df_filtered["Note"], palette=colors)
elif chart_type == "Barres 3D":
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection='3d')
    x_pos = np.arange(len(df_filtered))
    ax.bar(x_pos, df_filtered["Note"], zs=0, zdir='y', alpha=0.8, color=colors)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(df_filtered["Nom"])
    ax.set_xlabel("Nom de l'étudiant")
    ax.set_ylabel("Note")
    ax.set_zlabel("Valeur")
elif chart_type == "Points":
    sns.scatterplot(x=df_filtered["Nom"], y=df_filtered["Note"], palette=colors, s=100)
elif chart_type == "Histogramme":
    sns.histplot(df_filtered["Note"], kde=True, color=colors[0])  # Utiliser une couleur pour l'histogramme
elif chart_type == "Boxplot":
    sns.boxplot(x=df_filtered["Nom"], y=df_filtered["Note"], palette=colors)
elif chart_type == "Violin":
    sns.violinplot(x=df_filtered["Nom"], y=df_filtered["Note"], palette=colors)
elif chart_type == "Area":
    sns.lineplot(x=df_filtered["Nom"], y=df_filtered["Note"], color=colors[0], lw=5)  # Utilisation d'une couleur
    plt.fill_between(df_filtered["Nom"], df_filtered["Note"], color=colors[0], alpha=0.5)  # Remplissage
elif chart_type == "Heatmap":
    corr_matrix = df_filtered.corr()  # Assuming correlation matrix for heatmap
    sns.heatmap(corr_matrix, annot=True, cmap=color_palette)
elif chart_type == "Pairplot":
    sns.pairplot(df_filtered, palette=color_palette)
elif chart_type == "Courbe avec cercles":
    sns.lineplot(x=df_filtered["Nom"], y=df_filtered["Note"], marker="o", color=colors[0])  # Courbe avec des cercles
elif chart_type == "Zigzag":
    # Ajouter une variation rapide des données pour créer un zigzag
    zigzag_data = np.array(df_filtered["Note"])
    zigzag_data = np.interp(np.arange(0, len(zigzag_data) * 2), np.arange(0, len(zigzag_data)), zigzag_data)
    sns.lineplot(x=np.arange(len(zigzag_data)), y=zigzag_data, marker="o", color=colors[0])  # Courbe en zigzag
elif chart_type == "Diagramme Circulaire":
    plt.pie(df_filtered["Note"], labels=df_filtered["Nom"], autopct='%1.1f%%', colors=colors)

# Ajouter un titre et des labels
plt.title(f"Notes des étudiants de {ecole_choisie} (Note Min: {note_min})")
plt.xlabel("Nom de l'étudiant")
plt.ylabel("Note")

# Ajouter la légende en bas et changer sa couleur selon la palette choisie
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles=handles, labels=df_filtered["Nom"], loc="upper center", bbox_to_anchor=(0.5, -0.05), ncol=3)

# Afficher le graphique dans Streamlit
st.pyplot(plt)

