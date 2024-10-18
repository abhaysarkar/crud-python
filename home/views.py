
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from home.models import Person
from home.serializers import PersonSerializer

@api_view(['GET', 'POST'])
def index(request):

    courses = {
        'course_name': 'python',
        'learn': ['Flask', 'Django', 'Spring_Boot', 'FastApi'],
        'course_provider': 'GFG'
    }

    if request.method == 'GET':
        print("You are hitting GET method")
    elif request.method == 'POST':
        print("you are hitting POST method")
    return Response(courses)



@api_view(['GET', 'POST'])
def register(request):

    if request.method == 'GET':
        # Logic for GET request (optional, can be removed if only POST is needed)
        return Response({"message": "Use POST request to submit data"})

    elif request.method == 'POST':
        # Logic for POST request
        try:
            data = request.data  # Fetch the JSON data sent in the POST request
            
            # Extract data from the JSON
            name = data.get('name')
            age = data.get('age')
            email = data.get('email')

            # Personobj = Person.objects.get(email="abhaysheets@gmail.com")
            # print(Personobj.id)
            # print(Personobj.age)
            # print(Personobj.email)
            # print(Personobj.name)

            # Save the data to the database
            person = Person.objects.create(name=name, age=age, email=email)
            person.save()

            # Person = Person(id=id, name=name, age=age, email=email)  # Create a new instance but not saved yet
            # Person.save()  # Now save it to the database

            return Response({"message": "Person created successfully", "Person": data}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['PUT'])     
def editRegisteredUser(request):

    try:
        data = request.data  # Fetch the JSON data sent in the POST request
        # Extract data from the JSON
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')

        personObj = Person.objects.get(email=email)
        print(personObj.id)
        print(personObj.age)
        print(personObj.email)
        print(personObj.name)

        id = personObj.id

        person = Person(id=id, name=name, age=age, email=email)
        person.save()

        return Response({"message": "User created successfully", "user": data}, status=status.HTTP_200_OK)

    except person.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)  
    except Person.MultipleObjectsReturned:
        print("Multiple users found with the same name.")      



# API function to retrieve a user by email
@api_view(['GET'])
def get_user_by_email(request, email):
    try:
        # Strip any newline or whitespace from the email
        email = email.strip()
        user = Person.objects.get(email=email)
        # Return the user data (you can modify the format as needed)
        return JsonResponse({'email': user.email, 'name': user.name, 'age': user.age}, status=status.HTTP_200_OK)
    except Person.DoesNotExist:
        # Return a 404 response if the user is not found
        return JsonResponse({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_all_users(request):
    users = Person.objects.all()  # Retrieve all records from User table
    serializer = PersonSerializer(users, many=True)  # Serialize the queryset
    return Response(serializer.data)  # Return the serialized data

    # return Response("jai shree krishna")


@api_view(['DELETE'])
def delete_user_by_email(request):
    try:
        data = request.data  # Fetch the JSON data sent in the POST request
        # Extract data from the JSON
        email = data.get('email')

        user = Person.objects.get(email=email)
        print(user.id)
        print(user.age)
        print(user.email)
        print(user.name)

        #write logic to delete record
        user.delete()

        return Response({"message": "User user deleted successfully", "user": data}, status=status.HTTP_200_OK)

    except Person.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)  
    except Person.MultipleObjectsReturned:
        print("Multiple users found with the same name.")
