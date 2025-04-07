const Footer = () => {
  const currentYear = new Date().getFullYear()
  
  return (
    <footer className="bg-gray-800 text-white py-6">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0">
            <h2 className="text-xl font-bold">FastAPI React Example</h2>
            <p className="text-gray-400 mt-1">A modern full-stack application</p>
          </div>
          
          <div className="text-center md:text-right">
            <p>&copy; {currentYear} FastAPI React Example</p>
            <p className="text-gray-400 mt-1">Built with FastAPI and React</p>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer
