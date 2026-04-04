"use client"

import { Nav } from "@/components/layout/nav"
import { Footer } from "@/components/layout/footer"
import { ScrollProgress } from "@/components/shared/scroll-progress"
import { Opening } from "@/components/sections/opening"
import { ProblemSection } from "@/components/sections/problem"
import { SolutionSection } from "@/components/sections/solution"
import { HowItWorksSection } from "@/components/sections/how-it-works"
import { ComparisonSection } from "@/components/sections/comparison"
import { StackSection } from "@/components/sections/stack"
import { RoadmapSection } from "@/components/sections/roadmap"

export default function Home() {
  return (
    <main>
      <ScrollProgress />
      <Nav />
      <Opening />
      <ProblemSection />
      <SolutionSection />
      <HowItWorksSection />
      <ComparisonSection />
      <StackSection />
      <RoadmapSection />
      <Footer />
    </main>
  )
}
