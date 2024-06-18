import { useEffect, useState } from 'react';
import { View, Text, Button, Input, YStack, Card, H3, XStack, Form, Image, CardHeader, ScrollView,} from 'tamagui';
import { useNavigation, Link } from 'expo-router';
import * as ImagePicker from 'expo-image-picker';
import { addImage, addRecipe } from 'api/recipes';
import { StyleSheet } from 'react-native';

//Front end page that adds a new recipe to the database

export default function add() {
    //form state
    const [image, setImage] = useState(null);
    const [Recipe, setRecipe] = useState({
        name: '',
        ingredients: '',
        instructions: ''
    })
    //set header title
    const navigation = useNavigation();
    useEffect(() => {
        navigation.setOptions({
            headerTitle: 'Add Recipe'
        })
    }, [])
    //form submit function
    const addRecipeOnClick = async () => {
        let data = Recipe;
        let returns = await addRecipe(data);
        if (image){
            //add image to recipe
            let base64 = image;
            let responded = await addImage(base64, returns.id);
            console.log(responded);

        }


    }
    const pickImage = async () => {
        // No permissions request is necessary for launching the image library
        let result = await ImagePicker.launchImageLibraryAsync({
          mediaTypes: ImagePicker.MediaTypeOptions.All,
          allowsEditing: true,
          aspect: [4, 3],
          quality: 1,
        });
        if (!result.canceled) {
            setImage(result.assets[0].uri);
        }
      };
    

    return (
        <ScrollView>
            <Card
                margin='auto'
                padding='$3'
                mt='$10'
            >
                <CardHeader>
                {image && <Image source={{ uri: image }} style={styles.image} />}
                </CardHeader>

                <H3 >Add a new recipe</H3>

                <YStack
                    gap='$3'
                    p='$3'
                    flex={1}
                >
                    <Form
                        onSubmit={addRecipeOnClick}
                        gap='$3'
                    >
                        <Input size={'$3'} placeholder="Name" onChange={(e) => setRecipe({...Recipe, name: e.target.value})} />
                        <Input size={'$3'} placeholder="Ingredients" onChange={(e) => setRecipe({...Recipe, ingredients: e.target.value})} />
                        <Input size={'$3'} placeholder="Instructions" onChange={(e) => setRecipe({...Recipe, instructions: e.target.value})} />
                        <Button onPress={pickImage} > Pick Image</Button>
                        <Form.Trigger asChild >
                            <Button>Add Recipe</Button>
                        </Form.Trigger>
                    </Form>
                </YStack>
            </Card>
        </ScrollView>
    )
}
const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
    },
    image: {
      width: 200,
      height: 200,
    },
  });