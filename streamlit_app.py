import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import streamlit as st
import os

# Carrega a imagem
PATH_INV_OUTPUT_FILES = 'images/'


files = ['CE01.csv',
 'CE02.csv',
 'CE03.csv',
 'CE04.csv',
 'CE05.csv',
 'CE09.csv',
 'CE10.csv',
 ]

nomes_files = [nome.split(".")[0] for nome in files]

dfs = []
for file in files:
    aux = pd.read_csv(file, sep=",")
    dfs.append(aux)



# # Deslocamento em y do inicio dessas linhas em relação a linha de referência
# dy9, dy10 = 25, 45
# dfs[5]['Y'] = dfs[5]['Y'] + dy9 # Corrigindo o deslocamento da linha 9
# dfs[6]['Y'] = dfs[6]['Y'] + dy10 # Corrigindo o deslocamento da linha 10
z_values = dfs[3]['Z'].unique()
st.set_page_config(layout="wide", page_title="Visão 3D")
st.title('Visão 3D dos modelos geoelétricos\n')


# st.sidebar.write("SELECIONE AS SEÇÕES:")

CE01 = st.sidebar.checkbox('CE-01')
CE02 = st.sidebar.checkbox('CE-02')
CE03 = st.sidebar.checkbox('CE-03')
CE04 = st.sidebar.checkbox('CE-04')
CE05 = st.sidebar.checkbox('CE-05')
CE06 = st.sidebar.checkbox('CE-06')
CE07 = st.sidebar.checkbox('CE-07')
CE08 = st.sidebar.checkbox('CE-08')
CE09 = st.sidebar.checkbox('CE-09')
CE10 = st.sidebar.checkbox('CE-10')

col1, col2 = st.columns(2)
with col1:
    st.write('**Visão longitudinal**')

    Elevacao = st.slider('Elevação', 0, 90, 25)
    Azimute = st.slider('Azimute', 0, 360, 25)

    # Criando o gráfico 3D
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')

    index = 0
    x = np.linspace(dfs[index]['Y'].min(), dfs[index]['Y'].max(), 20)
    z = z_values
    X = dfs[index]['Y']
    Z = dfs[index]['Z']
    value = dfs[index]['rho']
    xi, zi = np.meshgrid(x, z)




    ### Adicionando o plot do index =0 na posição apropriada
    if CE01:
        alpha = st.sidebar.slider("Transparência CE-01", 0., 1., 0.3)
        y_value = 230
        ax.plot_surface(xi, np.full_like(xi, y_value), zi, alpha=0.1, color='blue')
        # Carregando a imagem
        img = plt.imread(PATH_INV_OUTPUT_FILES+'Linha1.png')
        img = np.flipud(img)
        x_img = np.linspace(dfs[index]['Y'].min(), dfs[index]['Y'].max(), img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(X_img, np.full_like(X_img, y_value), Z_img, facecolors=img, shade=False, alpha=alpha)
        ax.text(0.5, y_value, 1.1, "CE-01", color='red', fontsize=12, ha='center')
    #
    #
    #
    #
    if CE02:
        alpha = st.sidebar.slider("Transparência CE-02", 0., 1., 0.3)
        index = 1
        y_value = 210
        ax.plot_surface(xi, np.full_like(xi, y_value), zi, alpha=0.1, color='blue')
        img = plt.imread(PATH_INV_OUTPUT_FILES+'Linha2.png')
        img = np.flipud(img)

        x_img = np.linspace(dfs[index]['Y'].min(), dfs[index]['Y'].max(), img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(X_img, np.full_like(X_img, y_value), Z_img, facecolors=img, shade=False, alpha=alpha)
        ax.text(0.5, y_value, 1.1, "CE-02", color='red', fontsize=12, ha='center')
    #
    #
    #
    #
    if CE03:
        alpha = st.sidebar.slider("Transparência CE-03", 0., 1., 0.3)
        index = 2
        y_value = 160
        ax.plot_surface(xi, np.full_like(xi, y_value), zi, alpha=0.1, color='blue')
        img = plt.imread(PATH_INV_OUTPUT_FILES+'Linha3.png')
        img = np.flipud(img)
        # Define as coordenadas da imagem
        x_img = np.linspace(dfs[index]['Y'].min(), dfs[index]['Y'].max(), img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(X_img, np.full_like(X_img, y_value), Z_img, facecolors=img, shade=False, alpha=alpha)
        ax.text(0.5, y_value, 1.1, "CE-03", color='red', fontsize=12, ha='center')
    #
    #
    #
    #
    if CE04:
        alpha = st.sidebar.slider("Transparência CE-04", 0., 1., 0.3)
        index = 3
        y_value = 110
        ax.plot_surface(xi, np.full_like(xi, y_value), zi, alpha=0.1, color='blue')
        img = plt.imread(PATH_INV_OUTPUT_FILES+'Linha4.png')
        img = np.flipud(img)
        # Define as coordenadas da imagem
        x_img = np.linspace(dfs[index]['Y'].min(), dfs[index]['Y'].max(), img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(X_img, np.full_like(X_img, y_value), Z_img, facecolors=img, shade=False, alpha=alpha)
        ax.text(0.5, y_value, 1.1, "CE-04", color='red', fontsize=12, ha='center')
    #
    #
    #
    #
    if CE05:
        alpha = st.sidebar.slider("Transparência CE-05", 0., 1., 0.3)
        index = 4
        y_value = 70
        ax.plot_surface(xi, np.full_like(xi, y_value), zi, alpha=0.1, color='blue')
        img = plt.imread(PATH_INV_OUTPUT_FILES+'Linha5.png')
        img = np.flipud(img)
        # Define as coordenadas da imagem
        x_img = np.linspace(dfs[index]['Y'].min(), dfs[index]['Y'].max(), img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(X_img, np.full_like(X_img, y_value), Z_img, facecolors=img, shade=False, alpha=alpha)
        ax.text(0.5, y_value, 1.1, "CE-05", color='red', fontsize=12, ha='center')
    #
    #
    #
    #
    if CE09:
        alpha = st.sidebar.slider("Transparência CE-09", 0., 1., 0.3)
        index = 5
        y_value = 30
        ax.plot_surface(xi, np.full_like(xi, y_value), zi, alpha=0., color='blue')
        img = plt.imread(PATH_INV_OUTPUT_FILES+'Linha5.png')
        img = np.flipud(img)
        # Define as coordenadas da imagem
        x_img = np.linspace(dfs[index]['Y'].min(), dfs[index]['Y'].max(), img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(X_img, np.full_like(X_img, y_value), Z_img, facecolors=img, shade=False, alpha=alpha)
        ax.text(0.5, y_value, 1.1, "CE-09", color='red', fontsize=12, ha='center')
    #
    #
    #
    #
    if CE10:
        alpha = st.sidebar.slider("Transparência CE-10", 0., 1., 0.3)
        index = 6
        y_value = 0
        ax.plot_surface(xi, np.full_like(xi, y_value), zi, alpha=0., color='blue')
        img = plt.imread(PATH_INV_OUTPUT_FILES+'Linha5.png')
        img = np.flipud(img)
        # Define as coordenadas da imagem
        x_img = np.linspace(dfs[index]['Y'].min(), dfs[index]['Y'].max(), img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(X_img, np.full_like(X_img, y_value), Z_img, facecolors=img, shade=False, alpha=alpha)
        ax.text(0.5, y_value, 1.1, "CE-10", color='red', fontsize=12, ha='center')


    ax.view_init(elev=Elevacao, azim=Azimute)  # Define a elevação e o azimute inicial

    ax.set_ylabel("Y (m)")
    ax.set_xlabel("X (m)")
    ax.set_zlabel("profundidade")
    ax.set_ylim(0, 250)
    plt.tight_layout()
    st.pyplot(fig)

#######################################################
with col2:

    
    files = ['CE06.csv', 'CE07.csv', 'CE08.csv']
    nomes_files = [nome.split(".")[0] for nome in files]

    dfs = []
    for file in files:
        aux = pd.read_csv(file, sep=",")
        dfs.append(aux)

    dx6, dx7, dx8 = 20, 70, 120
    dfs[0]['X'] = dfs[0]['X'] + dx6 # Corrigindo o deslocamento da linha 6
    dfs[1]['X'] = dfs[1]['X'] + dx7 # Corrigindo o deslocamento da linha 7
    dfs[2]['X'] = dfs[2]['X'] + dx8 # Corrigindo o deslocamento da linha 8



    st.write("**Visão transversal**")

    Elevacao_lat = st.slider('Elevação_lat', 0, 90, 25)
    Azimute_lat = st.slider('Azimute_lat', 0, 360, 25)



    # Carrega a imagem
    PATH_INV_INPUT_FILES = 'images/'


    # Criando o gráfico 3D
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection='3d')

    if CE06:
        index = 0
        x = np.linspace(dfs[index]['X'].min(), dfs[index]['X'].max(), 20)
        z = z_values
        X = dfs[index]['X']
        Z = dfs[index]['Z']
        value = dfs[index]['rho']
        xi, zi = np.meshgrid(x, z)

        # Adicionando o plot do index = 0 na posição apropriada
        y_value = 20
        ax.plot_surface(np.full_like(xi, y_value), xi, zi, alpha=0.1, color='blue')
        # Carregando a imagem
        img = plt.imread(PATH_INV_INPUT_FILES+'Linha6.png')
        img = np.flipud(img)
        x_img = np.linspace(0, 230, img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(np.full_like(X_img, y_value), X_img, Z_img, facecolors=img, shade=False, alpha=0.8)
        ax.text(y_value, -20, max(Z_img.flatten()), "CE-06", color='red', fontsize=12, ha='center', va='bottom')

    if CE07:
        # Adicionando o plot do index = 1 na posição apropriada
        index = 1
        y_value = 70
        ax.plot_surface(np.full_like(xi, y_value), xi, zi, alpha=0.1, color='white')
        # Carregando a imagem
        img = plt.imread(PATH_INV_INPUT_FILES+'Linha7.png')
        img = np.flipud(img)
        x_img = np.linspace(0, 230, img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)
        ax.plot_surface(np.full_like(X_img, y_value), X_img, Z_img, facecolors=img, shade=False, alpha=0.8)
        ax.text(y_value, -20, max(z_img), "CE-07", color='red', fontsize=12, ha='center', va='bottom')

    if CE08:
        # Adicionando o plot do index = 2 na posição apropriada
        index = 2
        y_value = 120
        ax.plot_surface(np.full_like(xi, y_value), xi, zi, alpha=0.1, color='white')
        # Carregando a imagem
        img = plt.imread(PATH_INV_INPUT_FILES+'Linha8.png')
        img = np.flipud(img)
        x_img = np.linspace(0, 230, img.shape[1])
        z_img = np.linspace(min(z), max(z), img.shape[0])
        X_img, Z_img = np.meshgrid(x_img, z_img)

        ax.plot_surface(np.full_like(X_img, y_value), X_img, Z_img, facecolors=img, shade=False, alpha=0.8)
        ax.text(y_value, -10, max(Z_img.flatten()), "CE-08", color='red', fontsize=12, ha='center', va='bottom')

    ax.view_init(Elevacao_lat, Azimute_lat, 0)
    ax.set_ylabel("X (m)")
    ax.set_xlabel("Y (m)")
    ax.set_zlabel("profundidade")
    ax.set_ylim(0, 250)
    ax.set_xlim(150, 0)

    plt.tight_layout()
    st.pyplot(fig)
