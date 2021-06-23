
from sklearn import tree

# Rough 1 
# Smooth 0 
# Tennis 1 
# Cricket 2

def MarvellousML(weight,surface):

    #Step 1 & 2 : Data Gathering and Preparation
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],
				[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
				
    Label = [1,1,2,1,2,1,2,1,1,1,2,1,2,1]
    
	#Step 3: Algorithm Selection
    dobj = tree.DecisionTreeClassifier()
    
	#Step 4: Model Training
    dobj.fit(Features,Label)
    
	#Step 5: Model Testing
    result = dobj.predict([[weight,surface]])
    if (result == 1):
        print("Your object looks like Tennis ball")
    else:
        print("Your object looks like cricket ball")

def main():
    print("---------- Supervised Machine Learning -----------")
    print("Enter weight of object")
    weight = int(input())
    print("Enter surface type of object")
    surface = input()
    
    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("Invalid input")
        return
        
    MarvellousML(weight,surface)
    
if __name__ == "__main__":
    main()