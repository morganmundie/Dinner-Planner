
import { View, Text, Card } from 'tamagui';
import { Link } from 'expo-router';


export default function home() {
    return (
        <View>
            <Text>Home</Text>
            
            <Link href="/recipies"><Text>About</Text></Link>
            
        </View>
    )
}