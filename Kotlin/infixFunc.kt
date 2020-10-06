infix fun <T> List<T>.combineWith(other: List<T>): List<T> = this + other

fun main() {
    println(listOf("abc") combineWith listOf(1, 2, 3))
}
