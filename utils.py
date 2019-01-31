import numpy as np
import pandas as pd



def catch_collinear_variables(dataframe,threshold):
    matrix=dataframe.corr()
    extracted_matrix=matrix.where(np.triu(np.ones(matrix.shape),k=1).astype(bool))
    collinear_variables=[]
    for i in extracted_matrix.columns:
        if any(abs(extracted_matrix[i])>threshold):
            pair_variables=extracted_matrix.index[extracted_matrix.loc[:,i]>threshold].tolist()
            for _ in pair_variables:
                collinear_variables.append((i,_))
    return collinear_variables



def categorize_variables(df):
    
    remove_=[i for i in df.columns if df[i].nunique()==1]
    df=df.drop(remove_,axis=1)
    bools_=[i for i in df.columns if df[i].nunique()==2]
    ords_=[i for i in df.columns if df[i].nunique()<=5 and df[i].nunique()>2]
    nums_=[i for i in df.columns if df[i].nunique()>5]
    cats_=list(set(list(df.columns))-set(list(df._get_numeric_data().columns)))
    
    #converting bools to bool datatype
    for _ in bools_:
    df[_]=df[_].astype('bool')

    #converting ordinals to integer datatype
    for _ in ords_:
        df[_]=df[_].astype('int')

    #converting nums to float datatype
    for _ in nums_:
        df[_]=df[_].astype('float')
    
    
    return df




    










