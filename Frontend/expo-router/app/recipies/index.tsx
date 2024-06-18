

import { getRecipes } from "api/recipes";
import { Link } from "expo-router";
import { useEffect, useState } from "react";
import { Text, View, Card, XStack, Button, CardHeader, Image, CardBackground, H1, H3 } from "tamagui";


//View all recipies in the database listed out in cards

export default function recipies(){
    const [data, setData] = useState([{_id: {$oid:''}, name: '', ingredients: [], instructions: ''}]);
    useEffect(() => {
        getRecipes().then((response) => {
            console.log(response)
            setData(response);
        });
    }, []);
    
    

    return (
        <View>
            <Text>Recipies</Text>
            <Link href={'recipies/add'}><Button >Add Recipe</Button></Link>
            <XStack
                flexWrap="wrap"
                gap="$4"
            >
            {data.map((recipe) => {
                return (
                    
                        <Card
                            margin="$4"
                            padding="$4"
                            width="300px"
                            r="$4"
                            key={recipe._id.$oid}
                            padding="$0"
                            
                        >
                            <Card.Header padding = "$-0.25">
                            {
                                'image' in recipe ? <Image src={recipe.image} width="100%" height="200px" borderRadius='$5' margin='$0' borderBottomLeftRadius={0} borderBottomRightRadius={0}/>: null
                            }
                            <H3 padding="$2" paddingBottom="0">{recipe.name}</H3>
                            
                            </Card.Header>
                            
                            
                            
                            <Card.Footer padding="$4" paddingTop="0">
                                <Text>Instructions: {recipe.instructions}
                                <br/>
                                Ingredients: {recipe.ingredients} {/*recipe.ingredients.join(", ")*/}</Text>
                            </Card.Footer>
                            
                        </Card>
                    
                )
            })}
            </XStack>
        </View>
    )
}