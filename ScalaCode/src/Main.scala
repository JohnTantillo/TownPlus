object Main {
  def main(args: Array[String]): Unit = {
    val lot = new ParkingLot(1, 1)
    for(i <- 0 until 5) {
      lot.update()
      println(lot.toString())
      Thread.sleep(2000)
    }
  }
}
//    for( row <- lot.lot ){
//      for( spot <- row ){
//        println(spot.ID)
//        println(spot.distance)
//        print("\n")
//      }
//    }
//    println(lot.filledSpots)
//    println(lot.spots)
//    println(lot.percentFilled())
//    lot.filledSpots += 1
//    println(lot.filledSpots)
//    println(lot.percentFilled())
//println(lot.filledString())
//println(lot.toString())
//lot.spots(0).filled = true
//lot.update()
//println(lot.filledString())
//println(lot.toString())
//lot.spots(2).filled = true
//lot.update()
//println(lot.filledString())
//println(lot.toString())
//lot.spots(1).filled = true
//lot.update()
//println(lot.filledString())
//println(lot.toString())
//lot.spots(3).filled = true
//lot.update()
//println(lot.filledString())
//println(lot.toString())
//lot.spots(0).filled = false
//lot.update()
//println(lot.filledString())
//println(lot.toString())

//18 columns
//26 rows

//somethingicantype