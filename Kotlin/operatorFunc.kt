data class P(val a: Int = 0, val b: Int = 0)
operator fun P.unaryPlus() = P(a + 1, b + 1)
operator fun P.unaryMinus() = P(a - 1, b - 1)
operator fun P.not() = P(-a, -b)
operator fun P.plus(o: P) = P(a + o.a, b + o.b)
operator fun P.minus(o: P) = P(a - o.a, b - o.b)
operator fun P.times(o: P) = P(a*o.a, b*o.b)
operator fun P.div(o: P) = P(a / o.a, b / o.b)
operator fun P.inc() = P(a + 1, b + 1)
operator fun P.dec() = P(a - 1, b - 1)

fun main() {
    println(+P(1, 2)) // unaryPlus
    println(-P(1, 2)) // unaryMinus
    println(!P(1, 2)) // not
    println(P(1, 2) + P(3, 4)) // plus
    println(P(3, 4) - P(1, 2)) // minus
    println(P(3, 4) * P(1, 2)) // times
    println(P(3, 4) / P(1, 2)) // divide
    var o: P = P(1, 2)
    println("" + o++ + o-- + o) // increment & decrement
}
