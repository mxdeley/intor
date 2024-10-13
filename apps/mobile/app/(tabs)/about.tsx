import React from "react";
import {
  Text,
  SafeAreaView,
  StatusBar,
  View,
  Platform,
  StyleSheet,
  TextInput,
} from "react-native";

export default function HomePage() {
  return (
    <View style={styles.container}>
      <SafeAreaView style={styles.safeArea}>
        <StatusBar barStyle="dark-content" backgroundColor="#fff" />
        <View style={styles.content}>
          <Text>About Page</Text>
        </View>
      </SafeAreaView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  safeArea: {
    flex: 1,
  },
  content: {
    flex: 1,
    justifyContent: "flex-start",
    alignItems: "center",
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0,
  },
});
