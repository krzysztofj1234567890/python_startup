import pandas as pd
import numpy as np

def calculation( groups, weights, x ):
    result = 0 
    i = 0
    for group in groups: 
        group_name = "grps_"+str(i) 
        result += x['mean_'+group_name] * weights[i]
        i += 1 
    return result

def group_adjust(vals, groups, weights):
    """
    Calculate a group adjustment (demean).

    Parameters
    ----------

    vals    : List of floats/ints

        The original values to adjust

    groups  : List of Lists

        A list of groups. Each group will be a list of ints

    weights : List of floats

        A list of weights for the groupings.

    Returns
    -------

    A list-like demeaned version of the input values
    """

    # check inputs
    assert len(groups) == len(weights), "Invalid Operation" # size of groups and weights must be the same

    # create data dictionary
    data = {}
    data[ "vals" ] = vals
    i = 0 
    for group in groups:
        group_name = "grps_"+str(i)
        data[ group_name ] = group
        i += 1
    
    # create dataframe from dictionary
    df = pd.DataFrame(data)

    print( df)
    df = df.dropna() 
    print( "---- drop missig")
    print( df)

    # fill-in missing values with 0
    df['vals'] = df['vals'].fillna(0)
    # fill-in missing groups with 'missing'
    i = 0 
    for group in groups:
        group_name = "grps_"+str(i)
        df[ group_name ] = df[ group_name ].fillna("missing")
        i += 1

    # calculate means of each group
    column_count = 1 + len(groups)
    i = 0 
    for group in groups:
        group_name = "grps_"+str(i)
        mean = df.groupby( group_name )['vals'].transform('mean')
        df.insert( column_count + i, "mean_"+group_name, mean , True  ) 
        i += 1

    # Define an anonymous function to compute the weighted mean and add a new column with result
    df = df.assign(percentage = lambda x: ( calculation( groups, weights, x )  ))

    # Calculate result
    df = df.assign(result = lambda x: (x['vals'] - x['percentage'] ))

    print( df) 

    return df['result'].to_list()


# Create a sample DataFrame
data = {'ctry': [ 'USA', 'USA', 'USA' ],
        'state': [ 'MA' , 'MA' ,  'CT' ],
        'val': [1, 2, 3 ]
        }

weights = [.35, .65]

# data = {'Category': [ 'MA' , 'MA' ,  'CT' ],
#         'Values': [1, 2, 3 ]
#         }

df = pd.DataFrame(data)

print("---- df 1" )
print( df )

mean_ctry = df.groupby('ctry')['val'].transform('mean')
df.insert( 3, "mean_ctry", mean_ctry , True  ) 
mean_state = df.groupby('state')['val'].transform('mean')
df.insert( 4, "mean_state", mean_state , True  ) 


print("---- mean_ctry  " )
print( mean_ctry   )
print("---- mean_state " )
print( mean_state   )
print("---- df 2" )
print( df )

# Define a anonymous function to compute the weighted mean and add a new column with result
df = df.assign(percentage = lambda x: (x['mean_ctry'] * weights[0] + x['mean_state'] * weights[1] ))

# Calculate result
df = df.assign(result = lambda x: (x['val'] - x['percentage'] ))

print( "---- print final result" )
print( df )

# call function
print( "---- call function" )

# group_adjust([1, 2, 3 ], 
#             [ [ 'USA', 'USA', 'USA' ], [ 'MA' , 'MA' ,  'CT' ]],
#             [.35, .65] )

group_adjust([1, np.nan, 3, 5, 8, 7], 
            [[ 'USA', 'USA', 'USA', 'USA', 'USA', 'USA'], ['MA', 'RI', 'RI', 'CT', 'CT', 'CT'] ],
            [.65, .35] )
