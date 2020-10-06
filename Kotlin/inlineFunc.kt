inline fun <T> printlist(body: () -> List<T>) { println(body()) }

fun main() {
    printlist(fun():List<Any>{
        var a: MutableList<Any> = mutableListOf('a')
        a.add('b')
        a.add(1)
        a.add(1f)
        a.add("abc")
        return a
    })
}
