pluginManagement {
    includeBuild("build-plugins")
    repositories {
        // maven { setUrl("https://maven.aliyun.com/repository/public/") }
        // maven { setUrl("https://repo.huaweicloud.com/repository/maven/") }
        gradlePluginPortal()
        google()
        mavenCentral()
        maven { setUrl("https://jitpack.io") }
        // maven { setUrl("https://maven.scijava.org/content/repositories/public/") }
        mavenLocal()
    }
}
plugins {
    id("org.gradle.toolchains.foojay-resolver-convention") version "1.0.0"
}

/*includeBuild("D:/code/miuix") {
    dependencySubstitution {
        substitute(module("top.yukonga.miuix.kmp:miuix-core-android")).using(project(":miuix-core"))
        substitute(module("top.yukonga.miuix.kmp:miuix-ui-android")).using(project(":miuix-ui"))
        substitute(module("top.yukonga.miuix.kmp:miuix-material-android")).using(project(":miuix-material"))
        substitute(module("top.yukonga.miuix.kmp:miuix-blur-android")).using(project(":miuix-blur"))
        substitute(module("top.yukonga.miuix.kmp:miuix-preference-android")).using(project(":miuix-preference"))
        substitute(module("top.yukonga.miuix.kmp:miuix-icons-android")).using(project(":miuix-icons"))
        substitute(module("top.yukonga.miuix.kmp:miuix-navigation3-ui-android")).using(project(":miuix-nav"))
    }
}*/

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        // maven { setUrl("https://maven.aliyun.com/repository/public/") }
        // maven { setUrl("https://repo.huaweicloud.com/repository/maven/") }
        google()
        mavenCentral()
        maven { setUrl("https://jitpack.io") }
        // maven { setUrl("https://maven.scijava.org/content/repositories/public/") }
        mavenLocal()
    }
}

rootProject.name = "InstallerX-Revived"
include(
    ":app",
    ":app-process",
    ":hidden-api",
)
include(":baselineprofile")
