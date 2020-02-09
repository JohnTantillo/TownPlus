object Main {
  def main(args: Array[String]): Unit = {
    val lot = new ParkingLot(1, 1)
    while( true ) {
      Thread.sleep(2000)
      lot.update()
      //println("sent!")
    }
  }
}