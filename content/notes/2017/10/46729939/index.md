---
date: 2017-10-13 12:26:57
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/46729939/react-native-how-to-use-webview
tags:
- react-native
- questions
- stackoverflow
- software development
title: 'React Native: How to use Webview?'
---

I've been testing out the WebView component, but I can't seem to get it to render things.

Sample here: https://snack.expo.io/r1oje4C3-

    export default class App extends Component {
      render() {
        return (
          <View style={styles.container}>
            <Text style={styles.paragraph}>
              Change code in the editor and watch it change on your phone!
              Save to get a shareable url. You get a new url each time you save.
            </Text>
            <WebView source={{html: '<p>Here I am</p>'}} />        
            <WebView source={{ uri: 'http://www.google.com'}} />
          </View>
        );
      }
    }

When running the above example in Expo, neither of the two WebView components seem to render. What am I doing wrong?